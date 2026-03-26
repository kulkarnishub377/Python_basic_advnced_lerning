import strawberry
from typing import List, Optional
import resolvers

@strawberry.type
class Author:
    id: int
    name: str
    country: str
    
    @strawberry.field
    def books(self) -> List["Book"]:
        """Resolve books written by this author."""
        v = []
        # In a real app we would use SQL relationships or a dataloader
        from resolvers import books_db
        for b in books_db:
            if b.author_id == self.id:
                v.append(b)
        return v

@strawberry.type
class Book:
    id: int
    title: str
    year: int
    author_id: strawberry.Private[int] # Hide the raw FK from GraphQL
    
    @strawberry.field
    def author(self) -> Author:
        """Resolve the author for this specific book."""
        return resolvers.get_author_by_id(self.author_id)

@strawberry.type
class Query:
    @strawberry.field
    def books(self) -> List[Book]:
        return resolvers.get_books()
        
    @strawberry.field
    def authors(self) -> List[Author]:
        return resolvers.get_authors()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_book(self, title: str, year: int, author_id: int) -> Book:
        return resolvers.add_book(title, year, author_id)

# Combine Query and Mutation into a Schema
schema = strawberry.Schema(query=Query, mutation=Mutation)
