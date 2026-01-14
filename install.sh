#!/bin/bash
# CTF-PRO-AI Setup Script
echo -e "\e[32m[+] Installing System Dependencies...\e[0m"

sudo apt update
sudo apt install -y nmap exploitdb python3-pip binwalk exiftool gobuster metasploit-framework strings nm

echo -e "\e[32m[+] Installing Python Libraries...\e[0m"
pip3 install rich requests beautifulsoup4 pwntools

mkdir -p logs payloads/shells
chmod +x main.py

echo -e "\e[32m[+] Setup Finished. Execute: python3 main.py\e[0m"
