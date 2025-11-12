from abc import ABC, abstractmethod
from argparse import ArgumentParser, _SubParsersAction, Namespace
from typing import Callable, List

class CommandHandler(ABC):
    """
    Abstract base class for command handlers.

    :param name: The name of the command handler.
    """
    command_to_parser = {}

    def __init__(self, name: str):
        self.name: str = name

    @abstractmethod
    def get_commands(self) -> List[str]:
        """
        Get the list of commands supported by this handler.

        :returns: A list of supported commands.
        """
        pass

    def add_to_parser(self, subparsers: _SubParsersAction) -> None:
        """
        Add this handler's commands to the parser.

        :param subparsers: The subparsers object from the main parser.
        """
        for command in self.get_commands():
            # Check if a parser for this command already exists
            if command in CommandHandler.command_to_parser:
                command_parser = CommandHandler.command_to_parser[command]
            else:
                command_parser = subparsers.add_parser(command)
                command_subparsers: _SubParsersAction = command_parser.add_subparsers(
                    dest="subcommand"
                )
                CommandHandler.command_to_parser[command] = command_parser

            specific_command_parser: ArgumentParser = command_subparsers.add_parser(self.name)
            add_arguments_method: Callable[[ArgumentParser], None] = getattr(
                self, f"add_{self.name}_arguments", None
            )
            if add_arguments_method:
                add_arguments_method(specific_command_parser)
            specific_command_parser.set_defaults(func=getattr(self, command, None))

    def run(self, args: Namespace) -> None:
        """
        Execute the "run" command.

        :param args: The command-line arguments.
        """
        pass

    def upload(self, args: Namespace) -> None:
        """
        Execute the "upload" command.

        :param args: The command-line arguments.
        """
        pass

    def download(self, args: Namespace) -> None:
        """
        Execute the "download" command.

        :param args: The command-line arguments.
        """
        pass
