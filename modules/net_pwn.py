import subprocess
from core.brain import log

def network_enum(target):
    print(f"[*] Aggressive service fingerprinting on {target}...")
    log(f"Network Pwn started on {target}")
    subprocess.run(["nmap", "-sC", "-sV", "-Pn", target])
