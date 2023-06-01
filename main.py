from parse_args import parse_arguments
from colorama import Fore, Style

from url_validator import URLValidator


def main():
    url, timeout, show_errors = parse_arguments()
    validator = URLValidator(url, timeout, show_errors)

    is_website_up = validator.website_is_up()
    has_certificate = validator.get_certificate()

    website_status = f"{Fore.GREEN}Website is up.{Style.RESET_ALL}" if is_website_up else f"{Fore.RED}Website is down.{Style.RESET_ALL}"
    certificate_status = f"{Fore.CYAN}Website has a certificate.{Style.RESET_ALL}" if has_certificate else f"{Fore.YELLOW}Website does not have a certificate.{Style.RESET_ALL}"

    print(website_status)
    print(certificate_status)

if __name__ == "__main__":
    main()
