"""Main workflow module for SecurityGuard."""

import sys
from getpass import getuser

from rich.console import Console
from rich.panel import Panel
from rich.text import Text
from rich.box import ROUNDED

from securityguard.main.config import Config as MainConfig

class NotRootUserError(Exception):
    """Custom exception for when the user is not root."""

class MainWorkflow:
    """Class to handle main workflows for SecurityGuard."""

    def __init__(self):
        self.console = Console()
        try:
            self.config = MainConfig.from_file()
        except FileNotFoundError as e:
            error_msg = f"{e}"
            error_panel = Panel(
                error_msg,
                title="[bold red]Critical Error[/bold red]",
                style="danger",
                border_style="red"
            )
            self.console.print(error_panel)
            sys.exit(1)

        try:
            self.user_error_if_not_root()
        except NotRootUserError as e:
            error_msg = f"{e}"
            error_panel = Panel(
                f"[bold]Permission Denied:[/bold] {e}\n"
                "Please re-run this script using 'sudo'.",
                title="[bold red]Startup Error[/bold red]",
                style="danger",  # 'danger' is a built-in style (usually red)
                border_style="red"
            )
            self.console.print(error_panel)
            sys.exit(1)

    def display_welcome_panel(self):
        """Display a welcome panel in the console."""
        welcome_text = Text.from_markup(
            "[bold green]Welcome to SecurityGuard![/bold green]\n"
        )
        self.console.print(
            Panel(
                welcome_text,
                box=ROUNDED,
                title="SecurityGuard",
                subtitle="Your Security Companion"
            )
        )

    def check_current_user(self) -> str:
        """Check and return the current system user."""
        return getuser()

    def user_error_if_not_root(self):
        """Raise an error if the current user is not root."""
        if self.check_current_user() != "root":
            raise NotRootUserError('This operation requires root privileges.')

    def permission_check(self):
        """Check system permissions."""

    def service_check(self):
        """Check system services."""

    def config_check(self):
        """Check system configuration."""

    def rootkit_check(self):
        """Check for rootkits."""

    def main(self):
        """Execute the main workflow."""
        self.display_welcome_panel()
        self.permission_check()
        self.service_check()
        self.config_check()
        self.rootkit_check()
