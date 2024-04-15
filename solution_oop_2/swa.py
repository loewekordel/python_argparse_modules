from command_handler import CommandHandler

class SWACommandHandler(CommandHandler):
    def __init__(self):
        super().__init__('swa')

    def get_commands(self):
        return ['run', 'upload', 'download']

    def add_arguments(self, parser, command):
        if command == 'run':
            parser.add_argument('--force', action='store_true')
        elif command == 'upload':
            parser.add_argument('--overwrite', action='store_true')
        elif command == 'download':
            parser.add_argument('--latest', action='store_true')