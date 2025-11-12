import argparse
import logging
from mcdc import MCDCCommandHandler
from qac import QACCommandHandler
from swa import SWACommandHandler
from command_handler import CommandHandler


def setup_logging(verbose: bool = False) -> None:
    """Configure logging for the application."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )


def main() -> None:
    """
    Main function to handle command-line arguments and execute the appropriate command.
    """
    # Pre-parse for verbosity flag
    pre_parser = argparse.ArgumentParser(add_help=False)
    pre_parser.add_argument('-v', '--verbose', action='store_true', help='Enable verbose logging')
    pre_args, _ = pre_parser.parse_known_args()
    setup_logging(pre_args.verbose)

    logger = logging.getLogger(__name__)

    parser = argparse.ArgumentParser(
        description="CLI tool for managing MCDC, QAC, and SWA modules",
        parents=[pre_parser]
    )
    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
        help="Available commands"
    )

    handlers: list[CommandHandler] = [
        MCDCCommandHandler(),
        QACCommandHandler(),
        SWACommandHandler(),
    ]

    for handler in handlers:
        handler.add_to_parser(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func") and callable(args.func):
        try:
            args.func(args)
        except Exception as e:  # pylint: disable=broad-except
            logger.error("Command execution failed: %s", e, exc_info=pre_args.verbose)
            return 1
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
