from dataclasses import dataclass

## Use analyze(path_to_file, eventually_change_default_top=5)
## to get info about most frequent words

@dataclass()
class Results:

    def __post_init__(self):
        self.total_info={}
        # Dictionary about how many times each result was occured
        self.total_words_nr=0

    def __call__(self,word): 
        """object(result) = Click the result by +1"""
        if word not in self.total_info:
            self.total_info[word] = 0
        self.total_info[word] += 1
        self.total_words_nr += 1

    def set_show_top(self, limit):
        if isinstance(limit,int):
            self.show_top = limit

    def __str__(self):
        total_info_sorted=sorted(self.total_info.items(), key=lambda thing: thing[1],reverse=True)
        msg=""
        for index,(word,liczba) in enumerate(total_info_sorted,start=1):
            msg+= f"The word :{word} Liczba wystąpień :{liczba}\n"
            if index>=self.show_top:
                break
        msg+=f"Total words number : {self.total_words_nr}"
        return msg

def take_the_file(path):
    """Just returns the file """
    with open(path, "r") as file:
        from_file_data = file.read()
        return from_file_data

def analyze(path, top=5):
    results=Results()
    results.set_show_top(top)
    word=""
    for char in take_the_file(path):
        if char==" ":
            if len(word)>0:
                results(word)
            word=""
        else:
            word+=char
    print(results)
