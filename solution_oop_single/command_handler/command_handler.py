from abc import ABC, abstractmethod
from argparse import ArgumentParser, _SubParsersAction, Namespace
from typing import ClassVar, Dict, List, Tuple
import logging

logger = logging.getLogger(__name__)


class CommandHandler(ABC):
    """
    Abstract base class for command handlers.

    :param name: The name of the command handler.
    """
    # Store both the parser and subparsers to avoid accessing protected members
    # Use ClassVar to indicate this is a class variable
    _command_to_parser: ClassVar[Dict[str, Tuple[ArgumentParser, _SubParsersAction]]] = {}

    def __init__(self, name: str) -> None:
        self.name: str = name
        self._validate_handler()

    @abstractmethod
    def get_commands(self) -> List[str]:
        """
        Get the list of commands supported by this handler.

        :returns: A list of supported commands.
        """
        raise NotImplementedError("Subclasses must implement get_commands()")

    def _validate_handler(self) -> None:
        """
        Validate that the handler implements all commands it claims to support.

        :raises NotImplementedError: If a command is not implemented.
        """
        for command in self.get_commands():
            if not hasattr(self, command) or not callable(getattr(self, command)):
                logger.warning(
                    "%s declares command '%s' but doesn't implement it",
                    self.__class__.__name__,
                    command
                )

    @classmethod
    def reset_parser_cache(cls) -> None:
        """
        Reset the shared parser cache. Useful for testing.
        """
        cls._command_to_parser.clear()

    def add_to_parser(self, subparsers: _SubParsersAction) -> None:
        """
        Add this handler's commands to the parser.

        :param subparsers: The subparsers object from the main parser.
        """
        for command in self.get_commands():
            # Check if a parser for this command already exists
            if command in self._command_to_parser:
                _, command_subparsers = self._command_to_parser[command]
            else:
                command_parser = subparsers.add_parser(
                    command,
                    help=f"{command.capitalize()} operations"
                )
                command_subparsers: _SubParsersAction = command_parser.add_subparsers(
                    dest="module",
                    required=True,
                    help="Available modules"
                )
                self._command_to_parser[command] = (command_parser, command_subparsers)

            # Add module-specific parser
            module_parser: ArgumentParser = command_subparsers.add_parser(
                self.name,
                help=f"{self.name.upper()} module"
            )

            # Add command-specific arguments (fixed: use command name, not module name)
            self._add_command_arguments(module_parser, command)

            # Set the command function as default
            command_func = getattr(self, command, None)
            if command_func is not None and callable(command_func):
                module_parser.set_defaults(func=command_func)
                logger.debug("Registered %s.%s", self.name, command)

    def _add_command_arguments(self, parser: ArgumentParser, command: str) -> None:
        """
        Add command-specific arguments to the parser.

        :param parser: The argument parser.
        :param command: The command name (e.g., 'run', 'upload').
        """
        # Look for add_{command}_arguments method (e.g., add_run_arguments)
        add_arguments_method = getattr(self, f"add_{command}_arguments", None)
        if add_arguments_method is not None:
            add_arguments_method(parser)  # type: ignore[misc]
            logger.debug("Added arguments for %s.%s", self.name, command)
        else:
            logger.debug("No custom arguments for %s.%s", self.name, command)

    def run(self, args: Namespace) -> None:
        """
        Execute the "run" command.

        :param args: The command-line arguments.
        :raises NotImplementedError: If the handler doesn't implement this command.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement 'run' command"
        )

    def upload(self, args: Namespace) -> None:
        """
        Execute the "upload" command.

        :param args: The command-line arguments.
        :raises NotImplementedError: If the handler doesn't implement this command.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement 'upload' command"
        )

    def download(self, args: Namespace) -> None:
        """
        Execute the "download" command.

        :param args: The command-line arguments.
        :raises NotImplementedError: If the handler doesn't implement this command.
        """
        raise NotImplementedError(
            f"{self.__class__.__name__} does not implement 'download' command"
        )
