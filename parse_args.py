import argparse


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--url", required=True, help="URL of the website to check")
    parser.add_argument("-t", "--timeout", help="Timeout for the request in seconds (default: 5)", type=int, default=5)

    args = parser.parse_args()
    return args.url, args.timeout
