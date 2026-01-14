import requests
import subprocess
import os
from core.brain import log

def web_enum(url):
    """
    Advanced Web Intelligence Module.
    Handles traditional directory busting and modern SPA/API discovery.
    """
    # Clean the URL (Juice Shop often has /#/ at the end; we need the base)
    base_url = url.split('/#/')[0].rstrip('/')
    
    print(f"\n[bold cyan][*] Target Identified:[/bold cyan] {base_url}")
    log(f"Web Pwn started on {base_url}")

    try:
        # 1. Fingerprinting Headers
        print("[*] Fingerprinting Server...")
        r = requests.get(base_url, timeout=5)
        server = r.headers.get('Server', 'Unknown')
        tech_stack = r.headers.get('X-Powered-By', 'Unknown')
        
        print(f"    [+] Server: {server}")
        print(f"    [+] Technology: {tech_stack}")
        
        # 2. Strategic Directory/API Discovery
        # We exclude 503, 500, and 404 to fix the Heroku/Juice Shop 'Wildcard' error
        print("[*] Launching Gobuster (Excluding noisy status codes)...")
        
        # Path to wordlist (Kali default)
        wordlist = "/usr/share/wordlists/dirb/common.txt"
        
        if not os.path.exists(wordlist):
            print("[bold red][!] Wordlist not found! Please update the path in modules/web_pwn.py[/bold red]")
            return

        # Gobuster Command with Wildcard Handling (-b)
        cmd = [
            "gobuster", "dir",
            "-u", base_url,
            "-w", wordlist,
            "-b", "503,500,444,404", # Exclude common false positives
            "-q",                    # Quiet
            "--no-progress",         # No messy bars
            "-k"                     # Skip SSL verification for CTF labs
        ]

        # Execute Gobuster and stream output to console
        subprocess.run(cmd)

        # 3. Dedicated API Discovery (Dinger move for Juice Shop)
        print("\n[*] Checking for Common API Endpoints...")
        api_endpoints = [
            "/api/Challenges", "/rest/user/login", "/ftp", 
            "/api/Users", "/score-board", "/administration"
        ]
        
        for endpoint in api_endpoints:
            test_url = f"{base_url}{endpoint}"
            try:
                res = requests.get(test_url, timeout=3)
                if res.status_code == 200:
                    print(f"    [bold green][!] Interesting Endpoint Found: {test_url} (200 OK)[/bold green]")
                    log(f"Found endpoint: {test_url}")
            except:
                continue

    except requests.exceptions.RequestException as e:
        print(f"[bold red][-] Connection Error:[/bold red] {e}")
