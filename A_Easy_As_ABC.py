r11 = list(str(input()))
r22 = list(str(input()))
r33 = list(str(input()))

r = [r11, r22, r33]

res = []
for r1 in range(3):
    for c1 in range(3):
        for r2 in range(3):
            for c2 in range(3):
                for r3 in range(3):
                    for c3 in range(3):
                        
                        #CHECK ALL ARE DISTINCT
                        if (r1 == r2 and c1 == c2) or (r1 == r3 and c1 == c3) or (r2 == r3 and c2 == c3):
                            continue
                        
                        if abs(r1 - r2) <= 1 and abs(c1 - c2) <= 1 and abs(r2 - r3) <= 1 and abs(c2 - c3) <= 1:
                            res.append(r[r1][c1] + r[r2][c2] + r[r3][c3])
                        
                            # print(res)
print(min(res))
                        