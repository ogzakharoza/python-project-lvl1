install:
	poetry install
brain-games:
	poetry run brain-games
welcome-user:
	poetry run welcome-user
prompt:
	poetry add prompt
build:
	poetry build
publish:
	poetry publish --dry-run
package-install: 
	python3 -m pip install dist/*.whl
