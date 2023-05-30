from urllib.parse import urlparse


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
