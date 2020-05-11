with open("input.txt") as my_file:

  next(my_file)

  for line in my_file:

    str=line.split()
    Teams=str[1]
    FOR=str[9]
    AGAINST=str[10]
    var1=float(FOR)
    
    var2=float(AGAINST)
    diff=var1-var2
    print(Teams, FOR, AGAINST, diff)
    

       




