def div(thislist):
    answer = thislist[0]
    for x in (thislist[1:]):
        x = float(x)

        try:
            answer /= x
        except ZeroDivisionError:
            print("division by zero is impossible") 
        else:
            return(answer)


        
        
   
