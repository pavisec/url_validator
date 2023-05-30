from requests import ConnectionError, HTTPError, Timeout, RequestException, Session

from urllib.parse import urlparse
from colorama import Fore, Style

from config import USER_AGENT


class URLValidator:
    def __init__(self, url, timeout):
        self.url = self._validate_url(url)
        self.timeout = timeout

    @staticmethod
    def _validate_url(url):
        if not url.startswith(("http://www.", "https://www.")):
            url = f"https://www.{url}"
        result = urlparse(url)

        if result.scheme and result.netloc:
            return url
        else:
            raise ValueError("Invalid URL")
    
    def website_is_up(self):
        headers = {"User-agent", USER_AGENT}

        try:
            session = Session()
            response = session.get(self.url, headers=headers, timeout=self.timeout)
            return response.status_code == 200
        except Timeout:
            print(f"{Fore.LIGHTWHITE_EX}Request has timed out.{Style.RESET_ALL}")
        except ConnectionError:
            print(f"{Fore.LIGHTWHITE_EX}Failed to establish a connection.{Style.RESET_ALL}")
        except HTTPError:
            print(f"{Fore.LIGHTWHITE_EX}An HTTP error has occurred.{Style.RESET_ALL}")
        except RequestException:
            print(f"{Fore.LIGHTWHITE_EX}Something went wrong, try again later.{Style.RESET_ALL}")
        return False
