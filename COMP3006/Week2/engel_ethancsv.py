import csv


with open('data.csv','r') as q:
    reader =csv.reader(q)
    first=False
    greatestSsoFar=0.0
    greatestSrow=[]
    for rows in reader:
        if not first:
            first = True
        else:
            if float(rows[1])>greatestSsoFar:
                greatestSsoFar=float(rows[1])
                greatestSrow=rows
    print(greatestSrow)
