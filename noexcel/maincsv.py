# It's spirtually based off MisCell but more "interactive"
# It's more basic than Colrox and Thomas E. Krutz combined
import csv
import matplotlib.pyplot as plt

A1 = int(input("Please input the numerical value for A1. "))
B1 = int(input("Please do the same for B1. "))

# meta because for Smash4 MetaKnight

meta = input("please sum this: Press y for yes and n for no.")

if meta == "y":
    field = ['A1', 'B1', 'Meta']
    sum = A1 + B1
    sumint = int(sum)
    print(sum)
    rows = [A1, B1, sumint] 
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