"""Argparser to enter config path from CLI"""

import argparse


def create_arg_parser():
    """Creates and returns the ArgumentParser object"""

    parser = argparse.ArgumentParser(
        prog="log_analyzer.py",
        description='app for log parsing',
        # epilog="bottom placeholder"
    )
    parser.add_argument('--config', type=str, help='Path to the config file.')

    return parser
