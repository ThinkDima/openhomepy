docker_build:
	docker build -t openhomepy .

docker_run:
	PWD="$(pwd)"
	docker run --name openhomepy -it -p 80:80 -v ${PWD}:/app openhomepy

all: docker_build docker_run
