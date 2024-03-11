def fi(thelist, value):
    for index, element in enumerate(thelist):
        if str(element) == value:
            yield index
        elif isinstance(element, (list, tuple, set)):
            for deep_index in fi(element, value):
                yield (index,deep_index)

def showfi(thelist, value):
    for obj in fi(thelist, value):
        print (obj)

def crlist(): 
    tab=input("Give me this list or exit() (exaple--> [1,'b',3] <--) : ")
    tab=eval(tab) # Use eval to interpret the string input as a literal list
    return tab

# def show_normfi(thelist, value):
#     results = []
#     for index, element in enumerate(thelist):
#         if element == value:
#             results.append(index)
#         elif isinstance(element, (list, tuple, set)):
#             for deep_index in fi(element, value):
#                 results.append((index, deep_index))
#     return results

while True:
    subject=crlist()
    if isinstance(subject, list):
        search=input(" and enter for searching value : ")
        if search:
            showfi(subject,search)
