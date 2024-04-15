import argparse

def add_mcdc_commands(subparsers):
    parser = subparsers.add_parser('mcdc')
    parser.add_argument('--import-assessment', action='store_true')
    parser.add_argument('--check-safety', action='store_true')
    parser.add_argument('--force', action='store_true')
    parser.add_argument('--latest', action='store_true')