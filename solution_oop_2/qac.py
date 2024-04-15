from command_handler import CommandHandler

class QACCommandHandler(CommandHandler):
    def __init__(self):
        super().__init__('qac')

    def get_commands(self):
        return ['run', 'upload']

    def add_arguments(self, parser, command):
        if command == 'run':
            parser.add_argument('--recursive', action='store_true')
        elif command == 'upload':
            parser.add_argument('--update', action='store_true')