import subprocess
from core.brain import log

class ReconEngine:
    def __init__(self, target):
        self.target = target

    def run_full_recon(self):
        print(f"[*] Starting Multi-Stage Recon on {self.target}...")
        log(f"Recon started for {self.target}")
        try:
            res = subprocess.check_output(["nmap", "-sV", "-T4", self.target]).decode()
            print(res)
            log(res)
        except Exception as e:
            print(f"[-] Recon Error: {e}")
