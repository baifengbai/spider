i=1
def get(j):
    global i
    i=j
    while i<10:
        i = i + 1

if __name__=="__main__":

    get(i)
    print i