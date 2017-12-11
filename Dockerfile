# Template Dockerfile to build a simple python flask server which copies data files from ./app/ to ./home/
### Template extended for the recent-sites-txt2list docker image

FROM python:alpine
WORKDIR /home/
RUN pip install --upgrade flask flask_restful requests
# Extension
COPY /Users/Mike/Desktop/sites/* ./app/data/
# Mounting volume directly on run (allows for real-time updates) - so not required 
# COPY ./app/ /home/
EXPOSE 100
