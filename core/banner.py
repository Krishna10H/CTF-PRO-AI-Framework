from rich.console import Console
from rich.panel import Panel

def show_banner():
    console = Console()
    banner_text = """
    [bold cyan]
     ██████╗████████╗███████╗      █████╗ ██╗
    ██╔════╝╚══██╔══╝██╔════╝     ██╔══██╗██║
    ██║        ██║   █████╗  █████╗███████║██║
    ██║        ██║   ██╔══╝  ╚════╝██╔══██║██║
    ╚██████╗   ██║   ██║           ██║  ██║██║
     ╚═════╝   ╚═╝   ╚═╝           ╚═╝  ╚═╝╚═╝
    [/bold cyan]
    [bold green]Automated Exploitation & Recon Framework[/bold green]
    [dim]Author: Dasa Krishna Chaitanya | Version: 2.0[/dim]
    """
    console.print(Panel(banner_text, expand=False, border_style="blue"))
