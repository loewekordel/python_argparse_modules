import argparse
from mcdc import MCDCCommandHandler
from qac import QACCommandHandler
from swa import SWACommandHandler
from command_handler import CommandHandler


def main():
    """
    Main function to handle command-line arguments and execute the appropriate command.
    """
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    handlers: list[CommandHandler] = [
        MCDCCommandHandler(),
        SWACommandHandler(),
        QACCommandHandler(),
    ]

    for handler in handlers:
        handler.add_to_parser(subparsers)

    args = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
