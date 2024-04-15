import argparse

def add_qac_commands(subparsers):
    parser = subparsers.add_parser('qac')
    parser.add_argument('--import-assessment', action='store_true')
    parser.add_argument('--validate', action='store_true')
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--latest', action='store_true')