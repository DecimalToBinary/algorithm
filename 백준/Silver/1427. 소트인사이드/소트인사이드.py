N = input()
l = []
for i in N:
    l.append(i)

l.sort(reverse=True)
print(int(''.join(l)))