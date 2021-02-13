def main():
    import sys,csv

    values=[]

    with open(sys.argv[2], 'r') as f:
        reader = csv.reader(f, delimiter=" ", skipinitialspace=True)

        for row in reader:
                #print (row[int(sys.argv[1])])
            if float(row[int(sys.argv[1])])>-200:
                values.append(float(row[int(sys.argv[1])]))
    values.sort()
    #print(values)
    compute_stats(values)
    
def compute_stats(values):

        if values is None or len(values)==0:
            return None
        elif len(values)%2==1:
            o_median=values[int(len(values)/2)]
            o_avg = sum(values)/len(values)
            o_min=min(values)
            o_max=max(values)
        else:
            o_median=(values[int(len(values)/2)]+values[int(len(values)/2)-1])/2
            o_avg = sum(values)/len(values)
            o_min = min(values)
            o_max = max(values)


        print (o_min, o_max, o_avg, o_median)
        return (o_min, o_max, o_avg, o_median)

    #print('min: ',min(dailyAvgList),', max: ', max(dailyAvgList),', average: ', average, ', median: ', median)
if __name__ == '__main__':
        main()
