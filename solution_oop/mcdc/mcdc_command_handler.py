from argparse import ArgumentParser
from command_handler import CommandHandler
from .mcdc_executor import MCDCExecutor


class MCDCCommandHandler(CommandHandler):
    """
    Command handler for MCDC
    """

    def __init__(self):
        super().__init__("mcdc", MCDCExecutor("mcdc"))

    def get_commands(self):
        """
        Get the list of commands supported by this handler

        :returns: A list of supported commands
        """
        return ["run", "upload"]

    def add_run_arguments(self, parser: ArgumentParser):
        """
        Add arguments for the "run" command to the parser

        :param parser: The argument parser
        """
        parser.add_argument("--import-assessment", action="store_true")

    def add_upload_arguments(self, parser: ArgumentParser):
        """
        Add arguments for the "upload" command to the parser

        :param parser: The argument parser
        """
        parser.add_argument("--force", action="store_true")
