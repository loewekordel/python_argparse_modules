from command_handler import CommandHandler
from argparse import ArgumentParser
from argparse import Namespace

class QACCommandHandler(CommandHandler):
    """
    Command handler for QAC.

    :param name: The name of the command handler.
    """

    def __init__(self):
        super().__init__("qac")  # Initialize with the name "qac"

    def get_commands(self):
        """
        Get the list of commands supported by this handler.

        :returns: A list of supported commands.
        """
        return ["run", "upload", "download"]

    def add_run_arguments(self, parser: ArgumentParser):
        """
        Add arguments for the "run" command to the parser.

        :param parser: The argument parser.
        """
        # Add an optional argument for forcing run
        parser.add_argument("--force", action="store_true")

    def add_upload_arguments(self, parser: ArgumentParser):
        """
        Add arguments for the "upload" command to the parser.

        :param parser: The argument parser.
        """
        # Add an optional argument for overwriting upload
        parser.add_argument("--overwrite", action="store_true")

    def add_download_arguments(self, parser: ArgumentParser):
        """
        Add arguments for the "download" command to the parser.

        :param parser: The argument parser.
        """
        # Add an optional argument for downloading latest
        parser.add_argument("--latest", action="store_true")

    def run(self, args: Namespace):
        """
        Execute the "run" command.

        :param args: The command-line arguments.
        """
        # Print the command and arguments for demonstration purposes
        print(f"{self.name} run {args}")

    def upload(self, args: Namespace):
        """
        Execute the "upload" command.

        :param args: The command-line arguments.
        """
        # Print the command and arguments for demonstration purposes
        print(f"{self.name} upload {args}")

    def download(self, args: Namespace):
        """
        Execute the "download" command.

        :param args: The command-line arguments.
        """
        # Print the command and arguments for demonstration purposes
        print(f"{self.name} download {args}")