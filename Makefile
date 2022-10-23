#!make

.PHONY: default

default:
	pyinstaller -F main.py
