import os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__))
)

fh = open(os.path.join(__location__, 'sum.txt'))
a = 0

for line in fh.readlines():
    for i in line:
        if i.isdigit() == True:
            a += int(i)
print(f"Sum: {a}")

fh.close()