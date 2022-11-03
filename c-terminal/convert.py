#!/bin/env python3

import json

converted_data = ""
width = 0
height = 0

with open("../data.json") as f:
    data = json.load(f)
    for f, frame in enumerate(data):
        for row in frame:
            height += 1
            for col in row:
                width = len(row)
                converted_data += str(col)
            converted_data += "\n"
        print(f"FRAME {f}: WIDTH = {width}, HEIGHT = {height}")
        width = 0
        height = 0

with open("input.txt", "w") as f:
    f.write(converted_data)