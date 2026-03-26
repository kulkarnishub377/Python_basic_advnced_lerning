from elasticsearch import Elasticsearch

ES_URL = "http://localhost:9200"
INDEX_NAME = "products"

try:
    es = Elasticsearch(ES_URL)
    if not es.ping():
        raise ConnectionError
    ES_AVAILABLE = True
except Exception:
    es = None
    ES_AVAILABLE = False


def create_index():
    """Create the products index with custom mapping for full-text search."""
    if not ES_AVAILABLE:
        return
    if es.indices.exists(index=INDEX_NAME):
        return

    mapping = {
        "mappings": {
            "properties": {
                "name": {"type": "text", "analyzer": "standard"},
                "category": {"type": "keyword"},
                "price": {"type": "float"},
                "description": {"type": "text"},
            }
        }
    }
    es.indices.create(index=INDEX_NAME, body=mapping)


def index_product(product: dict):
    """Add a single product document to the index."""
    if not ES_AVAILABLE:
        return
    es.index(index=INDEX_NAME, body=product)


def search_products(query: str, size: int = 10):
    """
    Run a fuzzy multi-match query across name, category, and description fields.
    Returns results sorted by relevance score.
    """
    if not ES_AVAILABLE:
        return {"total_hits": 0, "results": [], "es_available": False}

    body = {
        "query": {
            "multi_match": {
                "query": query,
                "fields": ["name^3", "category^2", "description"],
                "fuzziness": "AUTO",
            }
        },
        "size": size,
    }

    resp = es.search(index=INDEX_NAME, body=body)

    results = []
    for hit in resp["hits"]["hits"]:
        source = hit["_source"]
        source["score"] = round(hit["_score"], 2)
        results.append(source)

    return {
        "total_hits": resp["hits"]["total"]["value"],
        "results": results,
    }
