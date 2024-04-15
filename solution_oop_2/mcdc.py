from command_handler import CommandHandler

class MCDCCommandHandler(CommandHandler):
    def __init__(self):
        super().__init__('mcdc')

    def get_commands(self):
        return ['run', 'upload']

    def add_arguments(self, parser, command):
        if command == 'run':
            parser.add_argument('--check', action='store_true')
        elif command == 'upload':
            parser.add_argument('--force', action='store_true')