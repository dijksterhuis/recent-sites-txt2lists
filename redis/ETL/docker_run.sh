path = '/Users/Mike/postgrad/Github/recent-sites-txt2lists'
cp /Users/Mike/Desktop/sites/*.txt $path/app/data/

docker run \
	-it --rm --name test --network recent-sites \
	-v $path/app/data:/home/data \
	recent-sites-redisload:0.1 /bin/ash -c 'python /home/load_redis.py'
