import pandas as pd
data = pd.read_csv('final.csv')



year = int(data.columns[3])
month = int(data.columns[4])
day = int(data.columns[5])

watt = 0.0
irms = 0.0
count = 0

for x in data:
    if int(data.columns[3]) == year  and int(data.columns[4]) == month and int(data.columns[5]) == day :
        watt += float(data.columns[2])
        irms += float(data.columns[1])
        count += 1

        if(int(data.columns[3]) > year):
            year+=1
            
        if(int(data.columns[4]) > month):
            month+=1

            
        print((data.columns[5]))
        if(int(data.columns[5]) > day):
            realIrms = irms/count
            realwatt =  watt/count
            day+=1
            print("Day IRms"+ realIrms)
            print("Day watt"+ realIrms)


        
        






















#irms,Voltage,watt,year,month,day,hour,minute
