
# Module for reading CSV's and OS
import csv
import os

 # Set path for file
csvpath = os.path.join('..','PyBank', 'raw_data', 'budget_data_2.csv')

# Reading using CSV module
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
    # To skip the header 
    next(csvreader, None)

    #Initialized counter to 0
    j=0
    i=0
    total =0
    # To keep Revenue list column
    revenue= []
    # To keep track on Revenue change 
    rev_change=[]
    # To keep track on date changes
    date_change=[]

    #To read date and revenue and write them in the new list and to find total number of months included in the dataset
    for row in csvreader:
        if row[i] != row[i+1]:
            date_change.append(str(row[0]))
            revenue.append(float(row[1]))
            #To find unique number of rows
            j+= 1
            # To find the sum of all the revenues
            total += float(row[1])    
          
    # To find difference, average, maximum and minimum among revenues
    for n in range(1,len(revenue)):
        rev_change.append(revenue[n] - revenue[n-1])
        avg_rev_change = sum(rev_change)/len(rev_change) 
        max_rev_change = max(rev_change)
        min_rev_change = min(rev_change)
        # To find index of maximum and minimum difference 
        maxpos = rev_change.index(max(rev_change)) 
        minpos = rev_change.index(min(rev_change)) 
    #Finding corresponding dates
    maxdatechange =date_change[maxpos+1]
    mindatechange =date_change[minpos+1]
 

    
    print("Financial Analysis")   
    print("--------------------")
    print('The total number of months included in the dataset' +" " + str(j))  
    print('The total amount of revenue gained over the entire period' +" " + str(total))
    print('The average change in revenue between months over the entire period' +" "+str(avg_rev_change))
    print("Greatest Increase in Revenue:", maxdatechange,"($", max_rev_change,")")
    print("Greatest Decrease in Revenue:", mindatechange,"($", min_rev_change,")")
            
with open("Output.txt", "w") as text_file:
    text_file.write("The total number of months included in the dataset" +" " + str(j)+'\n')
    text_file.write('The total amount of revenue gained over the entire period' +" " + str(total)+'\n')
    text_file.write('The average change in revenue between months over the entire period' +" "+str(avg_rev_change)+'\n')
    text_file.write("Greatest Increase in Revenue:{} $ ({}) \n" .format(maxdatechange,max_rev_change))
    text_file.write("Greatest Decrease in Revenue:{} $ ({}) \n" .format(mindatechange,min_rev_change))
  