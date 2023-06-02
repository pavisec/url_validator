[!["Buy Me A Coffee"](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/pavico)

# URL Validator

Validate the website's URL and check legitimate SSL certificate


## Features

- Validate the website URL
- Check Valid SSL Certificate
- Check Website's Status
- Show Error Messages
- Show Certificate


## Run Locally

Clone the project

```bash
  git clone https://github.com/pavisec/url_validator.git
```

Go to the project directory

```bash
  cd url_validator
```

Run the App

```bash
  python main.py -u example.com
```

## Commands (optional)

Request has timed out?

```bash
  python main.py -u example.com -t 10
```

Show error messages

```bash
  python main.py -u example.com --show-errors
```

Show certificate (not decoded)

```bash
  python main.py -u example.com --show-cert
```

## Authors

- [@pavisec](https://www.github.com/pavisec)

