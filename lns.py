import requests
from github import Github

# First create a Github instance using an access token
g = Github("your access token")

# Then get the authenticated user
user = g.get_user()

total_lines = 0

for repo in user.get_repos():
    contents = repo.get_contents("")
    while contents:
        file_content = contents.pop(0)
        if file_content.type == "dir":
            contents.extend(repo.get_contents(file_content.path))
        else:
            total_lines += len(requests.get(file_content.download_url).content.split("\n"))

print(f"Total lines: {total_lines}")
