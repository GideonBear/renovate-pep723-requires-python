# /// script
# requires-python = ">=3.15.1"
# dependencies = [
#   "requests==2.31.0",
# ]
# ///

import requests

print(requests.get("https://example.com", timeout=10).status_code)
