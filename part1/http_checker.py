#!/usr/bin/env python3

import requests
import sys

URLS = {
    "https://mock.codes/100",
    "https://mock.codes/200",
    "https://mock.codes/301",
    "https://mock.codes/400",
    "https://mock.codes/500",
}


def response_handler(response):
    code = response.status_code

    if 100 <= code < 400:
        print(f"[INFO] Status: {code}")
        print(f"[INFO] Body: {response.text.strip()}")
        print("-" * 40)
    elif 400 <= code < 600:
        raise Exception(
            f"HTTP client/server error: "
            f"status={code}, "
            f"url={response.url}, "
            f"body={response.text.strip()}"
        )
    else:
        print(
            f"[WARN] Unexpected status code {code}, "
            f"body: {response.text.strip()}")


def main():
    for url in URLS:
        try:
            resp = requests.get(url, timeout=10)
            response_handler(resp)
        except requests.exceptions.RequestException as network_err:
            print(
                f"[ERROR] Network issue for {url}: {network_err}",
                file=sys.stderr)
        except Exception as app_err:
            print(f"[ERROR] {app_err}", file=sys.stderr)


if __name__ == "__main__":
    main()
