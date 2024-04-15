from abc import ABC
from abc import abstractmethod
from argparse import _SubParsersAction, ArgumentParser, Namespace
from typing import Callable
from typing import Any


class CommandHandler(ABC):
    """
    Abstract base class for command handlers
    """

    def __init__(self, name: str, executor: Any):
        """
        Constructor

        :param name: The name of the command handler
        :param executor: The executor object that contains the methods to execute the commands
        """
        self.name: str = name
        self.executor = executor

    @abstractmethod
    def get_commands(self) -> list[str]:
        """
        Get the list of commands supported by this handler

        :returns: A list of supported commands
        """

    def add_to_parser(self, subparsers: _SubParsersAction) -> None:
        """
        Add this handler's commands to the parser

        :param subparsers: The subparsers object from the main parser
        """
        # Loop over each command
        for command in self.get_commands():
            print(f"Adding command {command} for handler {self.name}")
            # Create a new parser for this command
            command_parser: ArgumentParser = subparsers.add_parser(command)
            # Add subparsers for this command's subcommands
            command_subparsers: _SubParsersAction = command_parser.add_subparsers(
                dest="subcommand"
            )
            # Create a specific parser for this handler's name
            specific_command_parser: ArgumentParser = command_subparsers.add_parser(
                self.name
            )
            # Get the method to add arguments for this command
            add_arguments_method: Callable[[ArgumentParser], None] = getattr(
                self, f"add_{self.name}_arguments", None
            )
            # If the method exists, call it to add arguments
            if add_arguments_method:
                add_arguments_method(specific_command_parser)
            # Set the default function to be called when this command is used
            specific_command_parser.set_defaults(
                func=getattr(self.executor, command, None)
            )

    def run(self, args: Namespace) -> None:
        """
        Execute the "run" command

        :param args: The command-line arguments
        """
        pass

    def upload(self, args: Namespace) -> None:
        """
        Execute the "upload" command

        :param args: The command-line arguments
        """
        pass

    def download(self, args: Namespace) -> None:
        """
        Execute the "download" command

        :param args: The command-line arguments
        """
        pass
