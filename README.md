PyBank

Created a Python script for analyzing the financial records of a company. Based on the financial data called [budget_data.csv](PyBank/raw_data/budget_data2.csv). The dataset is composed of two columns: `Date` and `Profit/Losses`. 

*  Created a Python script that analyzes the records to calculate each of the following:

  * The total number of months included in the dataset
  * The total net amount of "Profit/Losses" over the entire period
  * The average change in "Profit/Losses" between months over the entire period
  * The greatest increase in profits (date and amount) over the entire period
  * The greatest decrease in losses (date and amount) over the entire period
* As an example, analysis will look similar to the below:

  ```text
  Financial Analysis
  ----------------------------
  Total Months: 86
  Total: $38382578
  Average  Change: $-2315.12
  Greatest Increase in Profits: Feb-2012 ($1926159)
  Greatest Decrease in Profits: Sep-2013 ($-2196167)
  ```

* Final script will print the analysis to the terminal and export a text file with the results.# 

PyBoss

Created a Python script to read csv file and store employee records in new csv file

*  Created a Python script that does the following:

  * Read csv file and store them in a list
  * Convert the states names in abbervations
  * Mask SSN
  * Store the formatted output in csv file

