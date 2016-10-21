from github import Github
from git import Repo
import os

if __name__ == "__main__":
  repo = Repo(os.getcwd())
  assert not repo.bare
  g = Github()
  urls = []
  for url in repo.remote().urls:
    urls.append(url)
  gh_repo = g.get_repo("testing-in-chrome/test_buck")
  print("Github repo: " + gh_repo.url)
  print("Active branch: " + str(repo.active_branch))

  print(gh_repo.commits_url)

  pr = gh_repo.create_pull("title1", "body1", "master",
                           str(repo.active_branch))
  print pr.url()