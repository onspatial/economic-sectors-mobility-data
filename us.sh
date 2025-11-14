#!/bin/bash
python code/data.py 1 5 us &
python code/data.py 2 5 us &
python code/data.py 3 5 us &
python code/data.py 4 5 us &
wait
python code/data.py 0 0 us
