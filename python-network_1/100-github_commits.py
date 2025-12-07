#!/usr/bin/python3
import sys
import requests

def main():
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    # GitHub API URL to get commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    # Get commits from the API (only first 10)
    response = requests.get(url, params={'per_page': 10})
    commits = response.json()

    for commit in commits:
        sha = commit.get('sha')
        # Try to get author name; fallback to commit author name
        author = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author}")

if __name__ == "__main__":
    main()
