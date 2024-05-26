t = int(input())

for test in range(t):
    s = str(input())
    h = int(s[0:2])


    a = "AM"

    if h >= 12:
        a = "PM"
        if h > 12:
            h -= 12

    if h == 0:
        h = 12

    if h < 10:
        h = "0" + str(h)
    
    s = str(h) + s[2:] + " " + a
    print(s)