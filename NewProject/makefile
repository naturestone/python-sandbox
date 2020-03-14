# makefile
# https://www.oreilly.de/german/freebooks/rlinux3ger/ch133.html

PYTHON = python
TEST = src/main.py

test: $(TEST)
	@$(PYTHON) $< test

dump:
	@echo "Code, Build, Test and Run Python Projects."

docgen: README.md 
	@pandoc $< 

print-version: dump
	@python3 --version 
	@$(PYTHON) --version
	@pip --version
	@which $(PYTHON)

requirements:
	sudo apt-get install pandoc 

.PHONY: dump test
