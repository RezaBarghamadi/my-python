print("Enter N && M for Create multiplication 😎")
n=int(input("Enter N :"))
m=int(input("Enter M :"))
def zarb(n,m):
    table = []
    for y in range(1, 10):
        sub_table = []
        for x in range(n, m):
            sub_table.append(x*y)
        table.append(sub_table)

    for t in table:
        print(t)

zarb(n,m)