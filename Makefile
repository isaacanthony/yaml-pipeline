build:
	@docker build -t yaml-pipeline .

run:
	@docker run \
		--name yaml-pipeline \
		--rm \
		-it \
		-v $(PWD):/src \
		yaml-pipeline python3 src/main.py $(pipeline)
