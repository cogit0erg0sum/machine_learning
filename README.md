## machine_learning
First machine learning project

# REQUIREMENTS  #
1. Github Account
2. Heroku Account
3.  VS Code IDE
4.  GIT CLI and Doc (https://git-scm.com/docs/user-manual)


# Creating conda environment
conda create -p venv python = 3.9.12 -y

# Installing requirements.txt for import libraries
pip install -r requirements.txt


# To add files to git
git add .

# add specific file 
git add <file_name>


# To ignore file or folder from git we can write name of file/folder in .gitignore file

# check git status 
git status


# check all version maintained by git 
git log

# commit changes 
git commit -m "message"

# push all changes to main branch
git push origin main 


# To check remote url
git remote -v

# To set up CI/CD pipeline



# Docker (https://docs.docker.com/go/guides/)
docker --version
docker --help

# BUILD DOCKER IMAGE
docker build -t <image_name>:,<tagname> .

> Note : image name should be lower case

# To list docker images
docker images

# Run docker image imageid for mac and 5000 for windows
docker run -p 3000:3000 -e PORT=3000 0a20a1a88978 


# docker ps to remove all containers
docker rm -f $(docker ps -aq)

# app on local host 
localhost:3000

# to check running containers check these commands in cmd
docker ps


# to stop container
docker stop container_id 



