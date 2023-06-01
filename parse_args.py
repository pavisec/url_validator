import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", "-u", required=True, help="URL of the website to check")
    parser.add_argument("--timeout", "-t", help="Timeout for the request in seconds (default: 5)", type=int, default=5)
    parser.add_argument("--show-errors", action="store_true", help="Show error messages")

    args = parser.parse_args()
    return args.url, args.timeout, args.show_errors
