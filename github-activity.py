import sys
import requests

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    headers = {"User-Agent": "Python-CLI-App"}
    try:
        response = requests.get(url, headers=headers, timeout=10)
        if response.status_code == 200:
            lastest_events = response.json()
            for event in lastest_events:
                if event['type'] == "PushEvent":
                    payload = event.get('payload', {})
                    repo_name = event['repo']['name']
                    if 'size' in payload:
                        commit_count = payload['size']
                    elif 'commits' in payload:
                        commit_count = len(payload['commits'])
                    elif 'head' in payload:
                        commit_count = 1
                    else:
                        commit_count = 0
                    if commit_count > 0:
                        print(f"- Pushed {commit_count} commit(s) to {repo_name}")
                elif event['type'] == "IssuesEvent":
                    repo_name = event['repo']['name']
                    print(f"- Opened a new issue in {repo_name}")
    except Exception as e:
        print(f"Error")
fetch_github_activity(sys.argv[1])
