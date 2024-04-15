# command_handler.py
class CommandHandler:
    def __init__(self, name):
        self.name = name

    def get_commands(self):
        raise NotImplementedError

    def add_to_parser(self, command_subparsers):
        for command in self.get_commands():
            module_subparser = command_subparsers[command].add_parser(self.name)
            self.add_arguments(module_subparser, command)

    def add_arguments(self, parser, command):
        raise NotImplementedError

    @staticmethod
    def add_handlers_to_parser(handlers, parser):
        subparsers = parser.add_subparsers(dest='command')

        commands = set(command for handler in handlers for command in handler.get_commands())

        command_subparsers = {command: subparsers.add_parser(command).add_subparsers(dest='module') for command in commands}

        for handler in handlers:
            handler.add_to_parser(command_subparsers)