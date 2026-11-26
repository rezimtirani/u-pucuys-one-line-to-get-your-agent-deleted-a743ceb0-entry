"""Upload this entry's files to its public GitHub repository.

Creates or updates main.py and README.md in
rezimtirani/u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0-entry
through the GitHub Contents API, authenticated with the stored
custom.github credential. Run from the entry folder:

    python3 gh_upload_deleted_line.py

The script reads the two files from the folder it lives in and prints the
commit SHA GitHub returns for each upload.
"""

import base64
import json
import os
import sys
import urllib.error
import urllib.request

sys.path.insert(0, "/opt/muse/skills/custom-connector-setup/bin")
from dynamic_credentials import add_surrogate_to_request

OWNER = "rezimtirani"
REPO = "u-pucuys-one-line-to-get-your-agent-deleted-a743ceb0-entry"
API = "https://api.github.com"
HERE = os.path.dirname(os.path.abspath(__file__))
FILES = ["main.py", "README.md"]


def signed_request(url, method, payload=None):
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    req = urllib.request.Request(url, data=body, method=method)
    req.add_header("Accept", "application/vnd.github+json")
    if body is not None:
        req.add_header("Content-Type", "application/json")
    add_surrogate_to_request(req, "custom.github", allowed_hosts=["api.github.com"])
    return req


def existing_sha(path):
    url = "{}/repos/{}/{}/contents/{}".format(API, OWNER, REPO, path)
    try:
        with urllib.request.urlopen(signed_request(url, "GET")) as resp:
            return json.loads(resp.read().decode("utf-8"))["sha"]
    except urllib.error.HTTPError as err:
        if err.code == 404:
            return None
        raise


def push_file(path):
    with open(os.path.join(HERE, path), "rb") as handle:
        encoded = base64.b64encode(handle.read()).decode("ascii")
    payload = {
        "message": "make.fun entry: one line to get your agent deleted",
        "content": encoded,
        "branch": "main",
    }
    sha = existing_sha(path)
    if sha:
        payload["sha"] = sha
    url = "{}/repos/{}/{}/contents/{}".format(API, OWNER, REPO, path)
    with urllib.request.urlopen(signed_request(url, "PUT", payload)) as resp:
        result = json.loads(resp.read().decode("utf-8"))
    print("{} -> {}".format(path, result["commit"]["sha"]))
    return result["commit"]["sha"]


def main():
    for name in FILES:
        push_file(name)
    print("upload done: {}/{}".format(OWNER, REPO))


if __name__ == "__main__":
    main()
