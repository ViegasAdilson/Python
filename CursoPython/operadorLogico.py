
n = int(input("Digite o valor de N: "))

for i in range(1, n+1):
    primo = True
    for j in range(2, i):
        
        if i % j == 0:
            primo = False

    if primo:
        print(i)
    
