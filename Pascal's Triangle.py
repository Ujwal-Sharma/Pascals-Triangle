def print_pascal_triangle(n):
    if n <= 0:
        return None
    elif n == 1:
        print("1")
        return None
    i = 1
    l = []
    t = []
    
    while i <= n:
        c = l[:]
        l += [1]
        d = 0
        
        while d < len(l):
            if d == 0:
                a = 0
                if len(c) == 0:
                    b = 1
                else:
                    b = c[d]
            elif d == len(l) - 1:
                b = 0
                if len(c) == 0:
                    a = 1
                else:
                    a = c[d - 1]
            else:
                a = c[d - 1]
                b = c[d]
            l[d] = a + b
            d += 1
        
        t.append(list(map(str,l)))
        i += 1

    maxi = max(list(map(len,t[n-1])))
    i = 0
    while i < n:
        
        d = 0
        while d < len(t[i]):
            t[i][d] += (maxi - len(t[i][d])) * " "
            d += 1
        
        t[i] = " ".join(t[i])
        t[i] = ((n - i - 1) + (maxi // 2) * (n - i - 1)) * " " + t[i]
        print(t[i])
        i += 1
        
print_pascal_triangle(int(input("Please enter the size of the Pascal's triangle: ")))
# A program to print a pascal's triangle with the size entered
