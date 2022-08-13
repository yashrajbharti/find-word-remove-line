
import fileinput
import sys

text = "<TimeSpan>"   # if any line contains this text, I want to remove the whole line.

x = fileinput.input(files="/Users/yashraj/Desktop/python/Located_Events.txt", inplace=1)
for line in x:
    if text in line:
        new_text = ""
        line = new_text
    sys.stdout.write(line)
x.close()