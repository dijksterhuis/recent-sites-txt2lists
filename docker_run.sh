# Docker run .sh script to launch a flask app from $path/app/

path=$1
docker run -d --rm -p 200:100 -v $path/app/:/home/ recent-site-lists:0.1 /bin/ash -c 'python /home/app.py'
