
import sys
import os
from rich.console import Console
from rich.panel import Panel
from rich.status import Status
from rich.text import Text
from rich.box import ROUNDED
import click
import logging
from securityguard.main.workflow import MainWorkflow

def main():
    """Entry point for the SecurityGuard CLI application."""
    MainWorkflow().main()
        # with Status("[status]Analyzing dependencies...[/status]", console=console, spinner="dots") as status:
        #     try:
        #         # --- START SCAN LOGIC SIMULATION ---
        #         import time
        #         total_packages = 200
        #         vulnerable_count = 5
        #         time.sleep(1)

        #         status.update("[status]Checking manifest files (e.g., package.json, requirements.txt)...[/status]")
        #         logger.info("Manifest files found and parsed.")
        #         time.sleep(1.5)

        #         status.update(f"[status]Querying vulnerability database for {total_packages} packages...[/status]")
        #         logger.debug(f"Querying external service for {total_packages} items...")
        #         time.sleep(2)

        #         status.update("[status]Generating final report...[/status]")
        #         time.sleep(1)
        #         # --- END SCAN LOGIC SIMULATION ---

        #         logger.info("Scan completed successfully.")

        #         # Print a Rich Panel summary
        #         summary_style = "green" if vulnerable_count == 0 else "danger"
        #         console.print(Panel(
        #             Text.from_markup(
        #                 f"[info]Total Packages Scanned:[/

if __name__ == "__main__":

    main()