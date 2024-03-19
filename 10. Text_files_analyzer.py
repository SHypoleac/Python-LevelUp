from dataclasses import dataclass

## Use analyze(path_to_file)
## to get info about most frequent words

@dataclass()
class Results:

    def __post_init__(self):
        self.str_limit=10
        self.total_info={}
        # Dictionary about how many times each result was occured
        self.total_words_nr=0

    def __call__(self,word): 
        """object(result) = Click the result by +1"""
        if word not in self.total_info:
            self.total_info[word] = 0
        self.total_info[word] += 1
        self.total_words_nr += 1

    def set_str_limit(self, limit):
        if isinstance(limit,int):
            self.str_limit = limit

    def __str__(self):
        total_info_sorted=sorted(self.total_info.items(), key=lambda thing: thing[1],reverse=True)
        msg=""
        for index,(word,liczba) in enumerate(total_info_sorted,start=1):
            msg+= f"The word :{word} Liczba wystąpień :{liczba}\n"
            if index>=self.str_limit:
                break
        msg+=f"Total words number : {self.total_words_nr}"
        return msg

def take_the_file(path):
    """Just returns the file """
    with open(path, "r") as file:
        from_file_data = file.read()
        return from_file_data

def analyze(path):
    results=Results()
    word=""
    for char in take_the_file(path):
        if char==" ":
            if len(word)>0:
                results(word)
            word=""
        else:
            word+=char
    results.set_str_limit(5)
    print(results)
