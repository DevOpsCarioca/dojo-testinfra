test:
	testinfra -v test_container.py --connection=docker --host=testinfra

build:
	docker build -t testinfra .

kill:
	docker rm -f testinfra

run: build
	docker run -d --name testinfra testinfra
