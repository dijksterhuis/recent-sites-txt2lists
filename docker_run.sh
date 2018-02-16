# Docker run .sh script to launch a flask app from $path/app/

path=$1'/app/'
echo $path
docker run -d --rm \
    -p 80:100 \
    -v $path:/home/ \
    --name recent-sites-flask \
    dijksterhuis/recent-sites:latest
