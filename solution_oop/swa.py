from command_handler import CommandHandler


# solution_oop/swa.py
class SWACommandHandler(CommandHandler):
    command_arguments = {
        "run": lambda parser: parser.add_argument("--force", action="store_true"),
        "upload": lambda parser: parser.add_argument(
            "--overwrite", action="store_true"
        ),
        "download": lambda parser: parser.add_argument("--latest", action="store_true"),
    }

    def __init__(self):
        super().__init__("swa")
