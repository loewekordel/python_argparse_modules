import argparse
from swa import add_swa_commands
from mcdc import add_mcdc_commands
from qac import add_qac_commands

def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='command')

    commands = {
        'run': [add_swa_commands, add_mcdc_commands, add_qac_commands],
        'upload': [add_mcdc_commands, add_qac_commands],
        'download': [add_mcdc_commands, add_qac_commands]
    }

    for command, module_funcs in commands.items():
        command_parser = subparsers.add_parser(command)
        module_subparsers = command_parser.add_subparsers(dest='module')
        for module_func in module_funcs:
            module_func(module_subparsers)

    args = parser.parse_args()

    # Handle the arguments here
    # ...

if __name__ == "__main__":
    main()