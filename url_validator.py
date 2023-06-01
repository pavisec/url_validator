import socket
import ssl

from requests import ConnectionError, HTTPError, Timeout, RequestException, Session
from urllib.parse import urlparse
from colorama import Fore, Style

from config import USER_AGENT


class URLValidator:
    def __init__(self, url, timeout, show_errors=False):
        self.url = self._validate_url(url)
        self.timeout = timeout
        self.show_errors = show_errors

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
        headers = {"User-agent": USER_AGENT}

        try:
            session = Session()
            response = session.get(self.url, headers=headers, timeout=self.timeout)
            return response.status_code == 200
        except Timeout:
            if self.show_errors:
                print(f"{Fore.LIGHTWHITE_EX}Request has timed out.{Style.RESET_ALL}")
        except ConnectionError:
            if self.show_errors:
                print(f"{Fore.LIGHTWHITE_EX}Failed to establish a connection.{Style.RESET_ALL}")
        except HTTPError:
            if self.show_errors:
                print(f"{Fore.LIGHTWHITE_EX}An HTTP error has occurred.{Style.RESET_ALL}")
        except RequestException:
            if self.show_errors:
                print(f"{Fore.LIGHTWHITE_EX}Something went wrong, try again later.{Style.RESET_ALL}")
        return False
    
    def get_certificate(self):
        result = urlparse(self.url)
        hostname = result.hostname

        try:
            cert = ssl.get_server_certificate((hostname, 443))
            return bool(cert)
        except ssl.SSLError:
            if self.show_errors:
             print(f"{Fore.LIGHTWHITE_EX}Unable to establish a secure connection to the website.{Style.RESET_ALL}")
        except socket.gaierror:
            if self.show_errors:
             print(f"{Fore.LIGHTWHITE_EX}Failed to resolve the hostname. Please check the website URL.{Style.RESET_ALL}")
        except ConnectionError:
            if self.show_errors:
             print(f"{Fore.LIGHTWHITE_EX}Failed to establish a connection.{Style.RESET_ALL}")
        except Exception:
            if self.show_errors:
             print(f"{Fore.LIGHTWHITE_EX}An error has occurred while retrieving the certificate.{Style.RESET_ALL}")
        return False
