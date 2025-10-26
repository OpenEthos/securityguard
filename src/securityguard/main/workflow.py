from pathlib import Path
from rich.console import Console
from rich.panel import Panel
from rich.status import Status
from rich.text import Text
from rich.box import ROUNDED
from getpass import getuser
from securityguard.main.config import Config as MainConfig

class NotRootUserError(Exception):
    """Custom exception for when the user is not root."""
    pass

class MainWorkflow:
    """Class to handle main workflows for SecurityGuard."""

    def __init__(self):
        self.console = Console()
        try:
            self.config = MainConfig.from_file()
        except FileNotFoundError as e:
            error_msg= f"{e}"
            error_panel = Panel(
                error_msg,
                title="[bold red]Critical Error[/bold red]",
                style="danger",
                border_style="red"
            )
            self.console.print(error_panel)
            exit(1)

        try:
            self.user_error_if_not_root()
        except NotRootUserError as e:
            error_msg= f"{e}"
            error_panel = Panel(
            f"[bold]Permission Denied:[/bold] {e}\nPlease re-run this script using 'sudo'.",
                title="[bold red]Startup Error[/bold red]",
                style="danger", # 'danger' is a built-in style (usually red)
                border_style="red"
            )
            self.console.print(error_panel)
            exit(1)

    def display_welcome_panel(self):
        """Display a welcome panel in the console."""
        welcome_text = Text.from_markup(
            "[bold green]Welcome to SecurityGuard![/bold green]\n"
        )
        self.console.print(Panel(welcome_text, box=ROUNDED, title="SecurityGuard", subtitle="Your Security Companion"))

    def check_current_user(self) -> str:
        """Check and return the current system user."""
        return getuser()
    
    def user_error_if_not_root(self):
        if self.check_current_user() != "root":
            exit(2)
        else:
            raise NotRootUserError('This operation requires root privileges.')

    def permission_check(self):
        pass

    def service_check(self):
        pass

    def config_check(self):
        pass

    def rootkit_check(self):
        pass

    def ssh_permit_root_login_check(self):
        pass

    def unusual_activity_check(self):
        pass

    def internet_check(self):
        pass

    def interface_check(self):
        pass

    def dns_posioning_check(self):
        pass

    def arp_posioning_check(self):
        pass

    def botnet_check(self):
        pass


    def main(self):
        self.display_welcome_panel()
        self.user_error_if_not_root()
        self.permission_check()
        self.service_check()
        self.config_check()
        self.rootkit_check()
        self.ssh_permit_root_login_check()
        self.unusual_activity_check()
        self.internet_check()
        self.interface_check()
        self.dns_posioning_check()
        self.arp_posioning_check()
        self.botnet_check()
        
