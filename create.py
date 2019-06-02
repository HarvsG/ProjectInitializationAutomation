import sys
import os
from github import Github

USER = os.environ.get('USER')
path = "/home/"+ USER + "/Documents/Projects/"
dirname = os.path.dirname(__file__)

with open(dirname + '/access_token.creds') as f:
    token = f.readline().strip()
    

def create():
    folderName = path + str(sys.argv[1])
    print("Creating folder{}".format(folderName))
    os.makedirs(folderName)
    user = Github(token).get_user()
    repo = user.create_repo(sys.argv[1], private=True)
    print("Succesfully created private repository {}".format(sys.argv[1]))

if __name__ == "__main__":
    create()
