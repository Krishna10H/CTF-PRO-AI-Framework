import os
import subprocess

def analyze_binary(path):
    if not os.path.exists(path):
        print("[-] File not found.")
        return
    print(f"[*] Performing Static Analysis on {path}...")
    os.system(f"file {path}")
    os.system(f"strings {path} | grep -iE 'flag|pass|user|key'")
    print("[*] Symbols Found:")
    subprocess.run(["nm", "-D", path])
