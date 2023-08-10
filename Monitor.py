import requests

URLS = {
    "Aden": "https://cloud.hiredscore.com/avanade/",
    # ... add all the names and URLs here
    "Verona": "https://cloud.hiredscore.com/vanderlande/"
}

EXPECTED_HTML = """<!doctype html>
<html>
...
</body>
</html>"""  # trimmed for brevity; make sure to include the full expected HTML here.

def check_url(name, url):
    try:
        # Check primary URL for 302 and expected HTML content
        response = requests.get(url, allow_redirects=False)
        if response.status_code != 302 or EXPECTED_HTML not in response.text:
            print(f"Failed: {name} ({url}) returned {response.status_code} or did not contain the expected HTML.")
            return False

        # Construct the second URL
        constructed_url = f"{url}/saml_sp/login_url?sourceUrl={url}"
        response2 = requests.get(constructed_url)
        if response2.status_code != 200:
            print(f"Failed: Checking constructed URL for {name} ({constructed_url}) returned {response2.status_code}.")
            return False

        return True
    except Exception as e:
        print(f"Error checking {name} ({url}): {e}")
        return False

success = all([check_url(name, url) for name, url in URLS.items()])

if not success:
    exit(1)  # Exit with error code
