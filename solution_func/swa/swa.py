import argparse

def add_swa_commands(subparsers):
    parser = subparsers.add_parser('swa')
    parser.add_argument('--import-assessment', action='store_true')