prev = 0
new = 0
iter = 0


def a(prev, new, iter):
    
    if iter == 100: exit() #Exits if the iteration counter exeeds the threshold

    newMem = new #Rembmbers the new number before the increase for the previous number after the increase

    new += prev #Increases the new number

    print(new) # Prints the increased number

    if new == 0: new = 1 #If the new number is 0 after the increase, make it one to prevent a infinite loop

    prev = newMem #Sets the previous number to what the new number was before the increase

    iter += 1   #Increases the iteration counter so it can break

    a(prev, new, iter) #Calls itself so it is recursive

a(prev, new, iter)






