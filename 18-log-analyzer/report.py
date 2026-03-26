from collections import Counter

def generate_report(ips, urls, statuses, total):
    """
    Renders the tallied frequency matrices cleanly onto terminal data matrices natively.
    """
    print(f"Total Requests Scanned: {total}")
    print("-" * 40)
    
    print("Most Frequent IP Addresses:")
    for ip, count in ips.most_common(3):
        print(f" - {ip:<15} | {count} requests")
        
    print("\nMost Requested URLs:")
    for url, count in urls.most_common(3):
        print(f" - {url:<15} | {count} requests")
        
    print("\nStatus Code Distribution:")
    for code, count in statuses.items():
        print(f" - Code {code} : {count}")
    print("-" * 40)
