def get_prime_of(thenumber):
    try:
        thenumber=int(thenumber)
    except ValueError:
        print("The given number must be an integer")
        thenumber=1
    thenumber=int(thenumber)
    tablica=[]
    liczba=2
    while thenumber>1:
        if thenumber%liczba==0:
            thenumber=thenumber/liczba
            tablica.append(liczba)
        else :liczba+=1
    return tablica

x=1
while x!="exit":
    x=input("Enter a number : ")
    print(get_prime_of(x))
print("Baja bongo! PA! :*")
