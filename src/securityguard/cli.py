import click
import logging
import sys
from rich.console import Console
from rich.logging import RichHandler
from rich.theme import Theme
from rich.status import Status
from rich.box import ROUNDED
from rich.panel import Panel
from rich.text import Text

# --- Configuration and Setup ---

# Define a custom Rich Theme for attractive terminal output
custom_theme = Theme({
    "info": "dim cyan",
    "warning": "magenta",
    "danger": "bold red",
    "success": "bold green",
    "status": "bold yellow",
})

# Initialize Rich Console, applying the custom theme
console = Console(theme=custom_theme)

def setup_logging(verbose: bool, debug: bool):
    """Sets up the logging configuration based on CLI options using RichHandler."""
    level = logging.WARNING
    if verbose:
        level = logging.INFO
    if debug:
        level = logging.DEBUG

    # Clear existing handlers to prevent duplicate output
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    # Configure the logger to use RichHandler for pretty output
    logging.basicConfig(
        level=level,
        format="%(message)s",
        datefmt="[%X]",
        handlers=[RichHandler(
            console=console,
            show_time=True,
            show_level=True,
            show_path=False,
            markup=True,
            enable_link_path=False
        )]
    )

    return logging.getLogger("securityguard")

# --- Click Group and Commands ---

@click.group(
    # Allow -h/--help for help text
    context_settings={"help_option_names": ["-h", "--help"]},
    # Invokes the function even if no subcommand is given (used for the welcome panel)
    invoke_without_command=True
)
# Global Options for the whole CLI
@click.option(
    '--verbose', '-v',
    is_flag=True,
    help='Enable verbose output (INFO level logging).',
)
@click.option(
    '--debug',
    is_flag=True,
    help='Enable highly detailed debug output (DEBUG level logging).',
)
@click.version_option(
    "1.0.0",
    "--version",
    "-V",
    prog_name="securityguard-cli"
)
@click.pass_context
def sg(ctx: click.Context, verbose: bool, debug: bool):
    """
    \b
    SecurityGuard CLI - A professional tool for scanning and analyzing project dependencies for vulnerabilities.

    Use 'sg scan --help' for command-specific options.
    """
    # Initialize logger and store it in the context object for subcommands
    logger = setup_logging(verbose, debug)
    ctx.ensure_object(dict)
    ctx.obj['LOGGER'] = logger
    ctx.obj['CONSOLE'] = console

    # Print a welcome message if no subcommand was provided
    if ctx.invoked_subcommand is None:
        console.print(Panel(
            Text.from_markup(
                "[success]Welcome to SecurityGuard CLI![/success]\n\n"
                "[info]Run 'sg --help' for a list of available commands.[/info]\n"
                "Current version: [bold]1.0.0[/bold]"
            ),
            title="[bold yellow]SecurityGuard[/bold yellow]",
            border_style="yellow",
            box=ROUNDED
        ))


@sg.command()
@click.argument(
    'path',
    type=click.Path(exists=True, file_okay=False, readable=True),
    default='.',
    required=False,
    metavar='PATH'
)
# Command-specific options
@click.option(
    '--recursive', '-r',
    is_flag=True,
    default=False,
    help='Scan subdirectories recursively for manifest files.',
)
@click.option(
    '--config', '-c',
    type=click.Path(exists=True, dir_okay=False),
    default=None,
    help='Specify a custom configuration file path (e.g., sg.json).',
)
@click.option(
    '--output', '-o',
    type=click.Path(dir_okay=False, writable=True),
    default='security_report.json',
    help='File path to write the detailed JSON scan results.',
    show_default=True
)
@click.pass_context
def scan(ctx: click.Context, path: str, recursive: bool, config: str | None, output: str):
    """
    Scans the specified PATH for security vulnerabilities in dependencies.

    PATH defaults to the current directory (.).
    """
    logger = ctx.obj['LOGGER']
    console = ctx.obj['CONSOLE']

    logger.info(f"Starting security scan for path: [bold cyan]{path}[/bold cyan]")
    logger.debug(f"Configuration file: {config or 'Not specified'}")
    logger.debug(f"Recursive mode: {recursive}")
    logger.debug(f"Report output file: [bold]{output}[/bold]")

    # Use Rich Status to provide visual feedback during the process
    # The spinner stops automatically when the 'with' block exits
    with Status("[status]Analyzing dependencies...[/status]", console=console, spinner="dots") as status:
        try:
            # --- START SCAN LOGIC SIMULATION ---
            import time
            total_packages = 200
            vulnerable_count = 5
            time.sleep(1)

            status.update("[status]Checking manifest files (e.g., package.json, requirements.txt)...[/status]")
            logger.info("Manifest files found and parsed.")
            time.sleep(1.5)

            status.update(f"[status]Querying vulnerability database for {total_packages} packages...[/status]")
            logger.debug(f"Querying external service for {total_packages} items...")
            time.sleep(2)

            status.update("[status]Generating final report...[/status]")
            time.sleep(1)
            # --- END SCAN LOGIC SIMULATION ---

            logger.info("Scan completed successfully.")

            # Print a Rich Panel summary
            summary_style = "green" if vulnerable_count == 0 else "danger"
            console.print(Panel(
                Text.from_markup(
                    f"[info]Total Packages Scanned:[/info] [bold white]{total_packages}[/bold white]\n"
                    f"[info]Vulnerabilities Found:[/info] [{summary_style}]{vulnerable_count}[/{summary_style}]"
                ),
                title="[bold white on black] SCAN SUMMARY [/bold white on black]",
                title_align="left",
                border_style=summary_style,
                box=ROUNDED
            ))

            if vulnerable_count > 0:
                console.print(f"\n[danger]Found {vulnerable_count} critical issues. Detailed report written to [bold]{output}[/bold][/danger]")
            else:
                console.print(f"\n[success]No critical vulnerabilities found! Report written to [bold]{output}[/bold][/success]")

            # Simulate writing the report file
            with open(output, 'w') as f:
                f.write(f'// Dummy report file generated for path: {path}\n')
                f.write(f'// Vulnerabilities: {vulnerable_count}\n')
                f.write(f'// Config: {config or "default"}\n')
                f.write('// ... detailed JSON output here ...')

        except Exception as e:
            # Log the error and exit with a non-zero status
            logger.error(f"[danger]An unexpected error occurred during scan: {e}[/danger]")
            sys.exit(1)

# Entry point for the CLI
if __name__ == '__main__':
    # Execute the CLI application
    sg(obj={})
