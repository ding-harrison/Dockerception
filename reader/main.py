filepath = "/data/sample.txt"

try:
    f = open(filepath, "r+")
    for line in f:
        print(line)
except IOError:
    f = open(filepath, "w+")
finally:
    f.close()
