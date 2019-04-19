# It's spirtually based off MisCell but more "interactive"
# It's more basic than Colrox and Thomas E. Krutz combined
import csv
import matplotlib.pyplot as plt

A1 = int(input("Please input the numerical value for A1. "))
B1 = int(input("Please do the same for B1. "))

# meta because for Smash4 MetaKnight

meta = input("please sum this: Press y for yes and n for no.")

if meta == "y":
    field = ['A1', 'B1', 'Add', 'Divide', 'Subtract', 'Multiply']
    sum = A1 + B1
    sumint = int(sum)
    print(sum)
    
    # Divison Also
    divide = A1 / B1
    divideint = int(divide)
    print(divide)
    
    # Subtract
    subtract = A1 - B1
    #Puts int(FOO)'s for a reason: So that Matplotlib does not throw up
    subtractint = int(subtract)
    print(subtract)
    
    #multiplies
    multiply = A1 * B1
    multiplyint = int(multiply)
    print(multiply)
    #writes to row, done because it makes stuff easier
    rows = [A1, B1, sumint, divideint, subtractint, multiplyint]    
    
    
    
    with open('yeetboi.csv', 'w') as export:  
        csvwrite = csv.writer(export, sum)
        csvwrite.writerow(field)
        csvwrite.writerow(rows)
    # want to be able to plot these values using matplotlib    
    with open('yeetboi.tsv', 'w') as exporttsv:
        tsvwrite = csv.writer(exporttsv, delimiter='\t')
        tsvwrite.writerow(field)
        tsvwrite.writerow(rows)
    x = []
    y = []
    plot = input("Do you wanna plot this graph. Say y for yes and n for no!")
    if plot == "y":
        with open('yeetboi.csv', 'r') as plotcsv:
            plots = csv.reader(plotcsv, delimiter=',')
            for plotrow in plots:
                x.append(plotrow[0])
                # does it on purpose because all the values are writtern in the 1 (count from 0) or 2 row (count from 1).
                y.append(plotrow[1])
                
        plt.plot(x, y, label = "yeetboi!")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Yeet Boi")
        plt.legend()
        plt.show()
    
else:
    pass 
    print("nope")