def get_prime_of():
    thenumber=input("Podaj liczbę : ")
    try: 
        if thenumber=="exit":
            print("Baja bongo! PA! :*")
            exit()
        thenumber=int(thenumber)
    except ValueError:
        print("Podana liczba musi być liczbą cąłkowitą")
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

while True:
    print(get_prime_of())