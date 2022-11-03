#!/bin/env sh

if [ ! -f "pyvenv.cfg" ]; then
    python3 -m venv .
fi

. ./bin/activate
./bin/pip3 install -r requirements.txt

arg=$1
if [ ! $arg ]; then
    arg="hi"
fi

if [ $arg = "run" ]; then
    ./bin/python3 main.py
fi