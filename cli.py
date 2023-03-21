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
        type=str,
        default=[],
        help="Input desired URLs",
    )
    parser.add_argument(
        "-f",
        "--input-file",
        metavar="FILE",
        type=str,
        default="",
        help="File URLs parser",
    )
    return parser.parse_args()

def display_check_result(result, url, error=""):
    """Display the result of a connectivity check"""
    print(f"Status ya URL: '{url}' ni: ", end="")
    if result:
        return '"Ipo Site"'
    return "'Haipo Site'"
    