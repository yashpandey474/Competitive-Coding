t = int(input())

for test in range(t):
    w, h = map(int,input().split())
    # HORIZONTAL POINTS
    h1 = list(map(int, input().split()))[1:]
    h2 = list(map(int, input().split()))[1:]


    # VERTICAL POINTS
    v1 = list(map(int, input().split()))[1:]
    v2 = list(map(int, input().split()))[1:]

    hm = max(h1[-1] - h1[0], h2[-1] - h2[0])
    vm = max(v1[-1] - v1[0], v2[-1] - v2[0])

    print(max(w*vm, h*hm))
