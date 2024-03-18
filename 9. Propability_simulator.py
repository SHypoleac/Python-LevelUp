from dataclasses import dataclass
import random

@dataclass()
class Results:
    dices:int
    walls:int

    def __post_init__(self):
        self.total_info={}
        # Dictionary about how many times each result was occured
        self.total_info={wynik:0 for wynik in range(self.dices,((self.dices*self.walls)+1))}
        self.total_nr_attemps=0

    def __call__(self,wynik): 
        self.total_info[wynik]+=1
        self.total_nr_attemps+=1

    def __str__(self):
        str=""
        for wynik,liczba in self.total_info.items():
            str+=f"Ilość oczek :{wynik} Liczba trafień :{liczba} Procent {(liczba/self.total_nr_attemps)*100}%\n"
        return str

def dice_roll(walls,dices,throws):
    results=Results(dices=dices,walls=walls)
    for attemp in range(throws):
        attemp=[]
        for dice in range(dices):
            # Throw the dice and append result into attemp list
            attemp.append(random.randint(1,walls))
        total_result=sum(attemp)
        results(total_result)
    print(results)
    
dice_roll(6,3,100)
            
            
            
