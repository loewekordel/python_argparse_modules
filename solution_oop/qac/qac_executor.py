from argparse import Namespace


class QACExecutor:
    """
    Executor for QAC commands
    """

    def __init__(self, name: str):
        """
        Constructor

        :param name: The name of the executor
        """
        self.name: str = name

    def run(self, args: Namespace):
        """
        Execute the "run" command

        :param args: The command-line arguments
        """
        print(f"{self.name} run {args}")

    def upload(self, args: Namespace):
        """
        Execute the "upload" command

        :param args: The command-line arguments
        """
        print(f"{self.name} upload {args}")

    def download(self, args: Namespace):
        """
        Execute the "download" command

        :param args: The command-line arguments
        """
        print(f"{self.name} download {args}")
