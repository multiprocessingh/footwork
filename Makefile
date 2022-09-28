.PHONY: deps
deps:
	pip install pip-tools 'pip<22' && pip-compile requirements.in --output-file requirements.txt

.PHONY: install
install:
	# setuptools and pip install throw an error when local packages are included in requirements.txt, so we instead
  # install the local package directly during the install step.
	pip install --upgrade 'pip<22' && pip install -e .

.PHONY: tests
tests:
	pytest tests
