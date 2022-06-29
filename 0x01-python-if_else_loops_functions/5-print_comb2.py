#!/usr/bin/python3
for numb in range(0, 100):
    if numb == 99:
        print("{:d}".format(numb))
    else:
        print("{}".format(str(numb).zfill(2)), end=', ')
