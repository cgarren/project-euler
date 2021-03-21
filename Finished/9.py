import sys
for a in range(0, 999):
    for b in range(0, 999):
        for c in range(0, 999):
            if a**2 + b**2 == c**2:
                print("Triplet:", a, b, c)
                if a + b + c == 1000:
                    print(a, b, c, "Product:", a*b*c)
                    sys.exit()
