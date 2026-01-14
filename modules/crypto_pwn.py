import base64
import codecs
import binascii
from core.brain import log

def analyze_crypto(data):
    """Core logic to decode strings."""
    print(f"\n[*] Analyzing Input: {data[:30]}...")
    log(f"Crypto analysis on: {data}")

    # 1. Base64
    try:
        b64_decoded = base64.b64decode(data, validate=True).decode('utf-8')
        print(f"[bold green][+] Base64 Decoded:[/bold green] {b64_decoded}")
    except: pass

    # 2. Hex
    try:
        hex_decoded = binascii.unhexlify(data.replace(" ", "")).decode('utf-8')
        print(f"[bold green][+] Hex Decoded:[/bold green] {hex_decoded}")
    except: pass

    # 3. ROT13
    print(f"[bold cyan][!] ROT13 Attempt:[/bold cyan] {codecs.encode(data, 'rot_13')}")

def crypto_menu():
    """This is the function main.py calls."""
    print("\n" + "="*40)
    print(" CRYPTO PWN - BY DASA KRISHNA CHAITANYA ")
    print("="*40)
    print("1) Analyze String (Base64, Hex, ROT13)")
    print("2) Analyze File")

    choice = input("\nChoice > ")

    if choice == "1":
        data = input("Paste string: ").strip()
        analyze_crypto(data)
    elif choice == "2":
        path = input("File path: ")
        try:
            with open(path, 'r') as f:
                analyze_crypto(f.read().strip())
        except Exception as e:
            print(f"[-] Error: {e}")
