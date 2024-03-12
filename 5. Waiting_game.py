from dataclasses import dataclass
import pendulum

@dataclass()
class SuchVariable:
    rec=7
    def __call__(self,new):
        if abs(new)<abs(self.rec):
            self.rec=new
    def __str__(self):
        return str(self.rec)
record=SuchVariable()

def accuracy(delta,goal):
    delta=delta-goal
    record(delta)
    if -0.1<= delta <=0.1:
        print ("$$$$$$$$$   FENOMENAL!   $$$$$$$$$")
    if -0.5 <= delta <= 0.5:
        print("         Great!")
    elif 0.5 < delta <= 1:
        print("         Good! But too slow!")
    elif -1 <= delta < -0.5:
        print("         Good! But too fast!")
    elif 1 < delta <= 3:
        print("         Too slow!")
    elif -3 <= delta < -1:
        print("         Too fast!")
    print(f"Yur delta was : {delta} and your record is {record}\n----------------------------------------")

print("*******    Welcome in waitng game!    *******\n"
      "Click Enter to start and wait specified number of seconds before next click!\n"
      "@@@@     Good Luck!     @@@@")
whaaat = input()
goal = pendulum.duration(seconds=3)
goal=goal.total_seconds()
start = pendulum.now()

while True:
    delta = pendulum.interval(start,pendulum.now())
    accuracy(delta.total_seconds(),goal)
    start= pendulum.now()
    whaaaat = input(f"NEXT CLICK IN : >>>  {goal}  <<< SECONDS")


