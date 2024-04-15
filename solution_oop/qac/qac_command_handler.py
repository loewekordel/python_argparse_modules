from command_handler import CommandHandler
from argparse import ArgumentParser
from .qac_executor import QACExecutor


class QACCommandHandler(CommandHandler):
    """
    Command handler for QAC
    """

    def __init__(self):
        super().__init__("qac", QACExecutor("qac"))

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
