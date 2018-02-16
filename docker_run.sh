# Docker run .sh script to launch a flask app from $path/app/

docker pull dijksterhuis/recent-sites:latest

txt_file_path=$1
echo "Mounting "$path" to /home/app/data/ on recent-sites-flask"
docker run -di --rm \
    -p 80:100 \
    -v $txt_file_path:/home/data/ \
    --name recent-sites-flask \
    dijksterhuis/recent-sites:latest \
    /home/app.py
