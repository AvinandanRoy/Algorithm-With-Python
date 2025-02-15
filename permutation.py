
def permutation(line , pocket=""):
    if len(line) == 0 :
        print(pocket) 
    else :
        for i in range(len(line)):
            letter = line[i]
            front = line[:i]
            back= line[i+1:]
            together = front + back 
            permutation(together, pocket+letter)

permutation("AVINANDAN ROY")
       