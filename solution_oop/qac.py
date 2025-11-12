from command_handler import CommandHandler


# solution_oop/qac.py
class QACCommandHandler(CommandHandler):
    command_arguments = {
        "run": lambda parser: parser.add_argument("--recursive", action="store_true"),
        "upload": lambda parser: parser.add_argument("--update", action="store_true"),
    }

    def __init__(self):
        super().__init__("qac")
