from command_handler import CommandHandler


# solution_oop/mcdc.py
class MCDCCommandHandler(CommandHandler):
    command_arguments = {
        "run": lambda parser: parser.add_argument("--check", action="store_true"),
        "upload": lambda parser: parser.add_argument("--force", action="store_true"),
    }

    def __init__(self):
        super().__init__("mcdc")
