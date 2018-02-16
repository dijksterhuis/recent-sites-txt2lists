# Template Dockerfile to build a simple python flask server which copies data files from ./app/ to ./home/
### Template extended for the recent-sites-txt2list docker image

FROM python:alpine
WORKDIR /home/
RUN pip install --upgrade flask flask_restful requests redis
# Copy flask data
COPY ./app/ /home/
RUN chmod u+x /home/app.py
EXPOSE 100