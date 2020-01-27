#Variables de base
n = 20000
l2 = list()
l3 = list()
# t = range(20000,30150) #t pour test
# print(n) #test

l2.append(n)
for x in l2:
    # n = n+1 #mal placé
    l2.append(n)
    # print("https://montrealcampus.ca?p=" + str(n))    #confirmation de la variable n
    l3.append("https://montrealcampus.ca?p=" + str(n))
    n = n+1
    if int(n) == 30151:
        break
print(*l3, sep = "\n")
print(len(l3))