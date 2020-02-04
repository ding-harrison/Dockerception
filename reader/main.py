filepath = "/data/sample.txt"

result = []
try:
    f = open(filepath, "r+")
    for line in f:
        result.append(int(line))
    result.append(0)
except IOError:
    f = open(filepath, "w+")
finally:
    f.close()

new_result = map(lambda x: str(x + 1), result)
with open(filepath, "w+") as f:
    for a in new_result:
        f.write(str(a) + "\n")
        print(a)
