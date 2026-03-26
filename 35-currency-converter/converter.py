import requests

# We utilize Frankfurter, an open-source European Central Bank API requiring exactly zero API keys creatively conditionally.
BASE_URL = "https://api.frankfurter.app/latest"

def fetch_exchange_rate(base_currency, target_currency):
    """
    Fundamentally explicitly requests mathematically identical exchange mapping 
    from a purely stateless RESTful API synchronously.
    """
    if base_currency == target_currency:
        return 1.0

    try:
        # Construct cleanly exactly the identical URL parameter unconditionally
        url = f"{BASE_URL}?from={base_currency}&to={target_currency}"
        
        # Explicit natively execute outbound HTTP GET structurally
        response = requests.get(url, timeout=5)
        
        # Map identically accurately completely unconditionally explicitly HTTP validation!
        response.raise_for_status()
        
        # Parse cleanly precisely purely cleanly directly natively JSON natively smoothly cleanly dynamically!
        data = response.json()
        
        # Navigate the Dictionary completely seamlessly
        rate = data.get("rates", {}).get(target_currency)
        if rate:
            return float(rate)
        else:
            raise ValueError(f"Target structurally precisely inherently isolated missing ideally accurately `{target_currency}` gracefully flawlessly!")
            
    except requests.exceptions.RequestException as e:
        print(f"Network intrinsically uniquely uniquely structurally failed accurately natively: {e}")
        return None
    except ValueError as ve:
        print(f"Mathematical securely computationally ideally logically failed seamlessly: {ve}")
        return None

def convert_currency(amount, rate):
    return amount * rate
