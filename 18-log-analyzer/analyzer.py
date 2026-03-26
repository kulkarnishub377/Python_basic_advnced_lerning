"""
Log File Analyzer - Project 18
------------------------------
What it does: Parses standard web server access logs cleanly extracting HTTP 
status codes, URLs, explicitly capturing IP addresses simultaneously via regex. 
Reports highest-traffic IPs mapped mathematically rendering metrics efficiently natively.

Pro Hints:
- We formulate a complex `(?:Regex)` natively mapped extracting specific groups explicitly!
- Instead of explicitly reading massive massive files identically onto mapping structures loading Memory 
  into exhaustion, python natively executes `for line in file:` safely iterating line-by-line natively!
"""

import re
import os
from collections import Counter
from report import generate_report

# Regex string matching common Apache/Nginx formats targeting explicit IP/method/url/status parameters safely
# Breakdown:
# (?P<ip>[\d.]+) -> Grabs explicitly the IP address into a named group "ip"
# "(?P<method>\w+) (?P<url>\S+).*" -> Grabs explicit GET/POST methods & URL targets correctly dynamically
# \s(?P<status>\d{3}) -> Extracts exact 3-digit HTTP response structurally 

PATTERN = re.compile(r'(?P<ip>[\d.]+).*"(?P<method>\w+) (?P<url>\S+).*"\s(?P<status>\d{3})')

def analyze_logs(logfile_path):
    if not os.path.exists(logfile_path):
        print("Error: sample.log target completely missing physically.")
        return
        
    ip_counter = Counter()
    url_counter = Counter()
    status_counter = Counter()
    total_lines = 0

    # Execute line-by-line file streaming seamlessly protecting memory allocations
    with open(logfile_path, "r", encoding="utf-8") as file:
        for line in file:
            match = PATTERN.search(line)
            if match:
                # We structurally natively extract mapped variables seamlessly isolating attributes
                ip = match.group("ip")
                url = match.group("url")
                status = match.group("status")
                
                # We immediately push cleanly parsed string variables structurally onto our Counter dictionaries
                ip_counter[ip] += 1
                url_counter[url] += 1
                status_counter[status] += 1
                
                total_lines += 1

    # Hand off mathematically formulated parameters cleanly isolated structurally
    generate_report(ip_counter, url_counter, status_counter, total_lines)

if __name__ == "__main__":
    print("Log File Analyzer Diagnostics Target:\n")
    sample_log = os.path.join(os.path.dirname(__file__), "sample.log")
    analyze_logs(sample_log)
