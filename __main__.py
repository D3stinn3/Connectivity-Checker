#!/usr/bin/python3

import sys
import pathlib
from .cli import read_user_cli_args, display_check_result
from .checker import site_iko_online

"""The python file provisions the 'Glue' code"""
"""The __main__.py file is the Entry-Point Script
Connecting CLI to Connectivity Check via
the command: python -m Connectivity-Checker"""

def main():
    user_args = read_user_cli_args()
    urls = get_website_urls(user_args)
    if not urls:
        print("Error: no URLs to check", file=sys.stderr)
        sys.exit(1)
    the_synchronous_check(urls)

def get_website_urls(user_args):
    urls = user_args.urls
    if user_args.input_file:
        urls += read_urls_from_file(user_args.input_file)
        print("URLs parsed successfully...")
    return urls

def read_urls_from_file(file):
    file_path = pathlib.Path(file)
    if file_path.is_file():
        with file_path.open() as urls_file:
            urls = [url.strip() for url in urls_file]
            if urls:
                return urls
            print(f"Error: Empty Input File, {file}", file=sys.stderr)
    else:
        print("Error: Input File Not Found", file=sys.stderr)
    return []

def the_synchronous_check(urls):
    for url in urls:
        error = ""
        try:
            result = site_iko_online(url)
        except Exception as e:
            result = False
            error = str(e)
        display_check_result(result=result, url=url, error=error)
        

if __name__ == "__main__":
    main()
            
    



