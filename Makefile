all: docker_build docker_run

docker_build:
	docker build -t openhomepy .

docker_run:
	PWD="$(pwd)"
	docker run --name openhomepy -it --rm -p 80:80 -v ${PWD}:/app openhomepy

up:
	docker start openhomepy
