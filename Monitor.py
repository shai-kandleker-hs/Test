import requests

URLS = {
    "Aden": "https://cloud.hiredscore.com/avanade/",
    # ... (add all the other name-URL pairs here) ...
    "Verona": "https://cloud.hiredscore.com/vanderlande/"
}


def check_url(name, url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print(f"Failed: {name} ({url}) returned {response.status_code}.")
            return False
        return True
    except requests.ConnectionError:
        print(f"Connection error for {name} ({url}).")
        return False
    except Exception as e:
        print(f"Error checking {name} ({url}): {e}")
        return False


success = all([check_url(name, url) for name, url in URLS.items()])

if not success:
    exit(1)  # Exit with an error code to let Jenkins know that the job failed
