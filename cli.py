#!/usr/bin/python3

import argparse

def read_user_cli_args():
    """Handle CLI arguments and options"""
    parser = argparse.ArgumentParser(
        prog="Connectivity-Checker",
        description="Website Availablity Checker"
    )
    parser.add_argument(
        "-u",
        "--urls",
        metavar="URLs",
        nargs="+",
        type = str,
        default=[],
        help="Input desired URLs"
    )
    return parser.parse_args()