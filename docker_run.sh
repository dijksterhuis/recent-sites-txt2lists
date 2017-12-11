# Docker run .sh script to launch a flask app from $path/app/

path=$1'/app/'
echo $path
docker run -d --rm -p 200:100 -v $path:/home/ --name recent-sites-flask recent-site-flask:0.1 /bin/ash -c 'python /home/app.py'
