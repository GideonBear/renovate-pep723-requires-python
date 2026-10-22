# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "requests==2.34.2",
# ]
# ///

import requests

print(requests.get("https://example.com", timeout=10).status_code)
