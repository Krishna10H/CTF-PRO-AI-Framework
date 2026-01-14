import sys
import os

# Ensure the root directory is in the path for clean imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from core.banner import show_banner
from core.brain import log
from core.recon_engine import ReconEngine
from modules.web_pwn import web_enum
from modules.net_pwn import network_enum
from modules.reverse_pwn import analyze_binary
from modules.exploit_db import find_cve
from modules.crypto_pwn import crypto_menu
from modules.forensics_pwn import forensics_menu  # New Forensic Import
from payloads.msf_gen import generate_payload

def main():
    # Displays your custom banner with "Dasa Krishna Chaitanya"
    show_banner()
    
    while True:
        print("\n" + "="*65)
        print(" [1] Auto-Recon  [2] Web Pwn      [3] Net Pwn")
        print(" [4] Reverse Eng [5] Exploit DB   [6] Payload Gen")
        print(" [7] Crypto Pwn  [8] Forensics    [9] Exit")
        print("="*65)
        
        cmd = input("CTF-PRO-AI > ")

        if cmd == "1":
            target = input("Target IP: ")
            ReconEngine(target).run_full_recon()
            
        elif cmd == "2":
            url = input("Target URL: ")
            web_enum(url)
            
        elif cmd == "3":
            target = input("Target IP: ")
            network_enum(target)
            
        elif cmd == "4":
            path = input("File Path for Reverse: ")
            analyze_binary(path)
            
        elif cmd == "5":
            svc = input("Search Exploit (e.g. SMB 3.1): ")
            print(find_cve(svc))
            
        elif cmd == "6":
            ip = input("LHOST (Attacker IP): ")
            port = input("LPORT: ")
            generate_payload(ip, port)
            
        elif cmd == "7":
            crypto_menu()
            
        elif cmd == "8":
            # Direct link to the hashing and metadata logic
            forensics_menu()
            
        elif cmd == "9":
            print("\n[!] Mission Terminated. Created by Dasa Krishna Chaitanya.")
            sys.exit()
            
        else:
            print("[-] Invalid Selection. Please try again.")

if __name__ == "__main__":
    main()
