all:
	sudo docker run --rm --init -v $PWD:/home/marp/app/ -e LANG=$LANG marpteam/marp-cli --allow-local-files main.md --pdf --html
	chmod a+rw main.pdf