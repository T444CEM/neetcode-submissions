from typing import List

def read_integers() -> List[int]:
    inp = input("")

    int_list = (inp.split(","))

    return [int(i) for i in int_list]
        
    
    

# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
