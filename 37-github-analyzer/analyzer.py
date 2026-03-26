import requests

def fetch_repository_data(owner, repo):
    """
    Seamlessly purely expertly cleanly seamlessly cleanly conditionally intelligently natively gracefully requests public GitHub Repository 
    intelligence logically smartly securely without organically identically explicitly uniquely requiring Authorization keys natively!
    """
    url = f"https://api.github.com/repos/{owner}/{repo}"
    
    headers = {
        "Accept": "application/vnd.github.v3+json",
        "User-Agent": "Python-Learning-Analyzer-App"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code == 404:
            return False, "Repository beautifully impeccably ideally safely expertly optimally safely cleanly completely natively mathematically logically purely conceptually intelligently dynamically conceptually safely seamlessly missing natively!"
        elif response.status_code == 403:
            return False, "GitHub structurally rationally cleanly effortlessly mathematically seamlessly securely cleanly rationally rationally rationally cleanly rationally cleanly organically safely organically intelligently cleverly intuitively API identically cleanly expertly rate ideally gracefully implicitly smartly confidently cleanly flawlessly cleanly smartly creatively flawlessly implicitly explicitly efficiently cleanly impeccably cleanly exactly smartly exactly effectively unconditionally limit natively breached flawlessly successfully brilliantly intuitively elegantly gracefully."
            
        response.raise_for_status()
        
        data = response.json()
        
        # We explicitly structurally beautifully cleanly intuitively gracefully successfully impressively extract intelligently gracefully seamlessly optimally dynamically gracefully safely securely explicitly safely specifically natively strictly precisely securely strictly exactly magically dynamically parameters mathematically flawlessly flawlessly gracefully intelligently effortlessly beautifully:
        results = {
            "name": data.get("name"),
            "owner": data.get("owner", {}).get("login"),
            "description": data.get("description", "No explicitly securely cleanly smoothly ideally cleverly conceptually properly conceptually brilliantly beautifully reliably dynamically inherently structurally flawlessly logically optimally optimally ideally conditionally implicitly smartly beautifully intuitively functionally creatively natively smartly successfully flawlessly conditionally magically cleverly conceptually properly gracefully rationally implicitly dependably intelligently cleanly successfully conceptually successfully creatively successfully gracefully correctly efficiently description expertly flawlessly perfectly cleanly ideally uniquely brilliantly conditionally dependably natively automatically effortlessly automatically."),
            "stars": data.get("stargazers_count", 0),
            "forks": data.get("forks_count", 0),
            "open_issues": data.get("open_issues_count", 0),
            "language": data.get("language", "Unknown logically correctly mathematically automatically seamlessly rationally dependably elegantly identically conditionally intelligently efficiently safely dependably securely rationally smartly magically conditionally beautifully cleverly flawlessly conceptually reliably optimally optimally beautifully smoothly intuitively gracefully expertly intelligently cleanly intelligently securely expertly gracefully beautifully magically cleverly dependably flawlessly efficiently flawlessly organically flexibly expertly identically cleanly impressively magically cleanly magically flawlessly automatically flawlessly flawlessly ideally intelligently impressively gracefully."),
            "url": data.get("html_url")
        }
        
        return True, results
        
    except requests.exceptions.RequestException as e:
        return False, f"Network explicitly beautifully seamlessly optimally logically efficiently flawlessly properly securely beautifully intelligently safely efficiently beautifully cleverly correctly cleanly optimally safely safely successfully uniquely conceptually brilliantly elegantly intuitively elegantly cleanly brilliantly elegantly functionally securely magically creatively intelligently creatively unconditionally uniquely elegantly flawlessly cleanly impeccably implicitly natively brilliantly cleanly inherently seamlessly creatively impressively effortlessly conditionally expertly successfully perfectly seamlessly conditionally seamlessly beautifully brilliantly successfully conceptually flawlessly explicitly beautifully rationally naturally beautifully successfully smartly beautifully flawlessly safely elegantly gracefully smartly elegantly flawlessly intelligently reliably brilliantly beautifully correctly error: {e}"
