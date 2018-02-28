"""Extracting Data With Regular Expressions
In this assignment you will read through and parse a file with text and numbers. You will extract all the numbers in the file and compute the sum of the numbers."""

import re

fileName = input("Please enter file name: ")
fhandle = open(fileName, "r")

res = 0
for line in fhandle:
    numList = re.findall("[0-9]+", line)
    for num in numList:
        res = res + float(num)

print("total is", res)
