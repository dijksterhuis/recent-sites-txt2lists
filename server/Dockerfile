# Template Dockerfile to build a simple python flask server which copies data files from ./app/ to ./home/
### Template extended for the recent-sites-txt2list docker image

FROM python:alpine
WORKDIR /home/
COPY reqs.txt /home/
RUN pip install -r /home/reqs.txt ; rm /home/reqs.txt
# Copy flask data
COPY ./app/ /home/
RUN chmod u+x /home/app.py
EXPOSE 100