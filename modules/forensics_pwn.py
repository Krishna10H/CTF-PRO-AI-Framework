import hashlib
from PIL import Image
from PIL.ExifTags import TAGS
from core.brain import log

def get_file_hashes(filepath):
    """Calculates MD5 and SHA256 hashes for a file."""
    md5_hash = hashlib.md5()
    sha256_hash = hashlib.sha256()
    
    try:
        with open(filepath, "rb") as f:
            # Read in chunks to handle large files (forensics images/PCAPs)
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
                sha256_hash.update(byte_block)
        
        print(f"\n[bold green][+] Integrity Hashes:[/bold green]")
        print(f"    MD5   : {md5_hash.hexdigest()}")
        print(f"    SHA256: {sha256_hash.hexdigest()}")
        log(f"Hashes for {filepath}: MD5={md5_hash.hexdigest()}")
    except Exception as e:
        print(f"[bold red][-] Hashing Error:[/bold red] {e}")

def extract_image_metadata(filepath):
    """Extracts EXIF metadata from images (GPS, Time, Camera)."""
    try:
        image = Image.open(filepath)
        info = image._getexif()
        
        if not info:
            print("[bold yellow][!] No EXIF metadata found in this image.[/bold yellow]")
            return

        print(f"\n[bold cyan][*] Forensic Metadata Extracted:[/bold cyan]")
        for tag_id, value in info.items():
            tag = TAGS.get(tag_id, tag_id)
            print(f"    {tag:20}: {value}")
            
    except Exception as e:
        print(f"[bold red][-] Metadata Error:[/bold red] {e}")

def forensics_menu():
    print("\n--- [ Forensic Investigation Module ] ---")
    path = input("Enter path to file/image: ").strip()
    
    if not os.path.exists(path):
        print("[-] File not found.")
        return

    # 1. Always hash the evidence first (Standard Procedure)
    get_file_hashes(path)
    
    # 2. If it's an image, dig deeper
    if path.lower().endswith(('.png', '.jpg', '.jpeg', '.tiff')):
        extract_image_metadata(path)
