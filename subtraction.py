def sub(thislist):
    answer = thislist[0]
    for x in (thislist[1:]):
        x = float(x)
        answer -= x
    return(answer)    