build:
	@docker build -t yaml-pipeline .

run:
	@docker run \
		--name yaml-pipeline \
		--rm \
		-e PYTHONDONTWRITEBYTECODE=1 \
		-it \
		-v $(PWD):/src \
		yaml-pipeline python3 -m yaml_pipeline.main $(pipeline)

# TESTS
test: test-pylint test-yapf test-pytest test-sample

test-pylint:
	@echo 'Running pylint...'
	@docker run \
		--name yaml-pipeline-test-pylint \
		--rm \
		-e PYTHONDONTWRITEBYTECODE=1 \
		-v $(PWD):/src \
		-w /src \
		wpengine/pylint:python-3.7 . --rcfile=.pylintrc
	@echo

test-yapf:
	@echo 'Running yapf...'
	@docker run \
		--name yaml-pipeline-test-yapf \
		--rm \
		-e PYTHONDONTWRITEBYTECODE=1 \
		-v $(PWD):/src \
		yaml-pipeline yapf --recursive --diff --style=.style.yapf .
	@echo "success!\n"

test-pytest:
	@echo 'Running pytest...'
	@docker run \
		--name yaml-pipeline-test-pytest \
		--rm \
		-e PYTHONDONTWRITEBYTECODE=1 \
		-v $(PWD):/src \
		yaml-pipeline pytest --durations=3 -p no:cacheprovider .
	@echo

test-sample:
	@echo 'Running sample pipeline...'
	@make -s run pipeline=iris
	@echo "success!\n"
