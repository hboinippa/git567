import requests
import json



def get_info(git_user):
    url = f"https://api.github.com/users/{git_user}/repos"
    response = requests.get(url)
    
    if response.status_code == 200:
        repositories = response.json()
        return [repo['name'] for repo in repositories]
    else:
        print(f"Failed to retrieve repositories for user {git_user}")
        return []

def get_data(git_user, repo_name):
    url = f"https://api.github.com/repos/{git_user}/{repo_name}/commits"
    response = requests.get(url)
    
    if response.status_code == 200:
        commits = response.json()
        return len(commits)
    else:
        print(f"Failed to retrieve commits for repo {repo_name}")
        return 0

if __name__ == "__main__":
    git_user = input("Enter GitHub username: ")
    repo_names = get_info(git_user)
    
    if repo_names:
        print("User: " + git_user)
        for repo_name in repo_names:
            number_of_commits = get_data(git_user, repo_name)
            print(f"Repo: {repo_name} Number of Commits: {number_of_commits}")
    else:
        print("No repositories found for user: " + git_user)
