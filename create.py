import sys
import os
from github import Github

path = "~/Documents/Projects/"

with open('myfile.txt') as f:
    token = f

def create():
    folderName = str(sys.argv[1])
    os.makedirs(path + str(sys.argv[1]))
    user = Github(token).get_user()
    repo = user.create_repo(sys.argv[1], private=True)
    print("Succesfully created private repository {}".format(sys.argv[1]))

if __name__ == "__main__":
    create()
