"""Entry point module for the SecurityGuard CLI application."""

from securityguard.main.workflow import MainWorkflow

def main():
    """Entry point for the SecurityGuard CLI application."""
    MainWorkflow().main()

if __name__ == "__main__":
    main()
