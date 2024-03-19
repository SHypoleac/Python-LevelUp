from dataclasses import dataclass
import random

## Use dice_roll(nr_of_walls, nr_of_dices, nr_of_throws)
## to generate info about simulation propability

@dataclass()
class Results:

    def __post_init__(self):
        """ Creates a dictionary about how many times each result was occured"""
        self.total_info={}
        self.total_nr_attemps=0

    def __call__(self,wynik):
        """
        object(result) =
        Click the result by +1
        """
        if wynik not in self.total_info:
            self.total_info[wynik] = 0
        self.total_info[wynik]+=1
        self.total_nr_attemps+=1

    def __str__(self):
        sorted_info=sorted(self.total_info.items(),key=lambda thing: thing[0])
        msg=""
        for wynik,liczba in sorted_info:
            msg+=f"Ilość oczek :{wynik} Liczba trafień :{liczba} Procent {(liczba/self.total_nr_attemps)*100}%\n"
        return msg

def dice_roll(walls,dices,throws):
    results=Results()
    for attemp in range(throws):
        attemp=[]
        for dice in range(dices):
            # Throw the dice and append result into attemp list
            attemp.append(random.randint(1,walls))
        total_result=sum(attemp)
        # Click the result by +1
        results(total_result)
    print(results)
    
dice_roll(6,3,1000)
            
            
            
