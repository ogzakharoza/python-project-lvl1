install:
	poetry install
brain-games:
	poetry run brain-games
prompt:
	poetry add prompt
build:
	poetry build
publish:
	poetry publish --dry-run
package-install: 
	python3 -m pip install dist/*.whl
lint:
        poetry run flake8
