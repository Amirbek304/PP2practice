def usual(n):
    for x in n:
        if 2 * 3 == int(x) or 3 * 5 == int(x) or 5 * 2 == int(x):
            return "Yes"
        else:
            return "No"
        
print(usual(input()))