I want a cli in python that fulfills the following requirements:
- cli commands should follow the following structure: command subcommand --arguments
- command can be: run, download, upload
- subcommand can be: swa, mcdc, qac
- The following commands should be implemented:
-- run swa can have the following arguments: --force
-- run qac can have the following arguments: --recursive
-- run mcdc can have the following arguments: --check
-- upload swa can have the following arguments: --overwrite
-- upload qac can have the following arguments: --update
-- download swa can have the following arguments: --latest
- the subcommands should be implemented in separate files e.g. swa.py, qac.py, mcdc.py
- The command/subcommand definition in argparse should be inside the swa, mcdc and qac modules because more modules will be added in the future and adding/removing modules should be as simple as possible
- It should be modular so that further modules can be added easily
- The solution should be advanced enough to be able to handle more commands and subcommands in the future
- The solution should be advanced like a senor dev would do it in a pythonic way
- Argparse should be used
- The solution should be flexible and modular
- Create a full example
- The module implementation should look like this:
```python
from command_handler import CommandHandler

class MCDCCommandHandler(CommandHandler):
    def __init__(self):
        super().__init__('mcdc')

    def get_commands(self):
        return ['run', 'upload']

    def add_run_arguments(self, parser):
        parser.add_argument('--import-assessment', action='store_true')

    def add_upload_arguments(self, parser):
        parser.add_argument('--force', action='store_true')
```