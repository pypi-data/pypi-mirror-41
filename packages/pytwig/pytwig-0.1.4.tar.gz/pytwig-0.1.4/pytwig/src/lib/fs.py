#author: stylemistake https://github.com/stylemistake

import os

def read(path, relative_to = None):
    if relative_to != None:
        path = os.path.dirname(os.path.realpath(relative_to)) + '/' + path
    with open(path, 'r') as file:
        return file.read()

def read_lines(path):
    with open(path, 'r') as file:
        return file.read_lines()

def read_binary(path):
    with open(path, 'rb') as file:
        return file.read()

def write(path, text):
    with open(path, 'w') as file:
        file.write(text)

#Everything below here is edited from the original document

def write_binary(path, text):
    with open(path, 'wb') as file:
        file.write(text)
