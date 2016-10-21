from github import Github
from git import Repo
import os
import getpass

if __name__ == "__main__":
  repo = Repo(os.getcwd())
  assert not repo.bare
  username = raw_input("Enter Github username: ")
  password = getpass.unix_getpass("Password: ")
  g = Github(username, password)
  urls = []
  for url in repo.remote().urls:
    urls.append(url)
  gh_repo = g.get_repo("testing-in-chrome/test_buck")
  print("Github repo: " + gh_repo.url)
  branch = str(repo.active_branch)
  print("Active branch: " + branch)

  print(gh_repo.commits_url)

  print(gh_repo.pulls_url)
  pr = gh_repo.create_pull(title="title1", body="body1", base="master",
                           head=branch)
  print pr.url
