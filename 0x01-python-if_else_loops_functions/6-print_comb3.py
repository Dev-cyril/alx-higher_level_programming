#!/usr/bin/python3
for numb in range(0, 100):
    if numb == 89:
        print(numb)
    else:
        print(str(numb).zfill(2), end=', ')