# main.py
import argparse
from mcdc import MCDCCommandHandler
from swa import SWACommandHandler
from qac import QACCommandHandler
from command_handler import CommandHandler

def main():
    parser = argparse.ArgumentParser()

    handlers = [MCDCCommandHandler(), SWACommandHandler(), QACCommandHandler()]

    CommandHandler.add_handlers_to_parser(handlers, parser)

    args = parser.parse_args()

    # Execute the appropriate command
    ...

if __name__ == '__main__':
    main()
