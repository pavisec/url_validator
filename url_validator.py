# Import necessary modules
import socket
import ssl

from requests import ConnectionError, HTTPError, Timeout, RequestException, Session

from urllib.parse import urlparse
from colorama import Fore, Style
from typing import Union

# Import User-agent config
from config import USER_AGENT


# This class is used to validate and fetch details about a URL
class URLValidator:
    # Initialize the object url, timeout, and the options to show errors and cert details
    def __init__(self, url, timeout: Union[int, float], show_errors=True, show_certificate=True):
        self.url = self._validate_url(url)
        self.timeout = timeout
        self.show_errors = show_errors
        self.show_certificate = show_certificate

    # Method to validate URL
    @staticmethod
    # Check if the scheme is present in the URL, if not prepend "https://"
    def _validate_url(url):
       if not urlparse(url).scheme:
          url = f"https://{url}"
       result = urlparse(url)

       if all([result.scheme, result.netloc]) and result.scheme in ["http", "https"]:
          netloc_parts = result.netloc.split(".")
          # Check if the netloc parts are valid, for example "www.example.com" is valid
          if len(netloc_parts) == 2 or (len(netloc_parts) > 2 and netloc_parts[0] == "www"): 
            return url
       else:
          # Raise an exception is the URL is invalid
          raise ValueError("Invalid URL")
    
    # Print error messages if show_errors flag is True
    def _print_error(self, message: str):
       if self.show_errors:
          print(f"{Fore.LIGHTWHITE_EX}{message}{Style.RESET_ALL}")
    
    # Check if a website is up by sending a GET request and checking for status code 200
    def website_is_up(self):
        headers = {"User-agent": USER_AGENT}

        try:
            session = Session()
            response = session.get(self.url, headers=headers, timeout=self.timeout)
            return response.status_code == 200
        except Timeout:
           self._print_error("Request has timed out.")
        except ConnectionError:
            self._print_error("Failed to establish a connection.")
        except HTTPError:
           self._print_error("An HTTP error has occurred.")
        except RequestException:
           self._print_error("Something went wrong, try again later.")
        return False
    
    # Fetch SSL certificate details of a website
    def get_certificate(self):
        result = urlparse(self.url)
        hostname = result.hostname

        try:
            cert = ssl.get_server_certificate((hostname, 443))
            has_certificate = bool(cert)
            if self.show_certificate:
               # Print certificate details if show_certificate flag is True
               print(f"\n{Fore.LIGHTMAGENTA_EX}{cert}{Style.RESET_ALL}")
            return has_certificate
        except ssl.SSLError:
            self._print_error("Unable to establish a secure connection to the website.")
        except socket.gaierror:
            self._print_error("Failed to resolve the hostname. Please check the website URL.")
        except ConnectionError:
            self._print_error("Failed to establish a connection.")
        except Exception:
            self._print_error("An error has occurred while retrieving the certificate.")
        return False
