#!/bin/sh

cd "$(dirname "$0")"
cd "$(dirname "$(readlink -f "$0")")"
python main.py "$@"
