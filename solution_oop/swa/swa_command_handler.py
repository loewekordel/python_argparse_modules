from argparse import ArgumentParser
from command_handler import CommandHandler
from .swa_executor import SWAExecutor

class SWACommandHandler(CommandHandler):
    """
    Command handler for SWA
    """

    def __init__(self):
        super().__init__("swa", SWAExecutor("swa"))

    def get_commands(self):
        """
        Get the list of commands supported by this handler

        :returns: A list of supported commands
        """
        return ["run", "upload", "download"]

    def add_run_arguments(self, parser: ArgumentParser):
        """
        Add arguments for the "run" command to the parser

        :param parser: The argument parser
        """
        parser.add_argument("--force", action="store_true")

    def add_upload_arguments(self, parser: ArgumentParser):
        """
        Add arguments for the "upload" command to the parser

        :param parser: The argument parser
        """
        parser.add_argument("--overwrite", action="store_true")

    def add_download_arguments(self, parser: ArgumentParser):
        """
        Add arguments for the "download" command to the parser

        :param parser: The argument parser
        """
        parser.add_argument("--latest", action="store_true")
