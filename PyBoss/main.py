import os
import csv
import datetime
filepath = os.path.join("..","PyBoss","raw_data", "employee_data1.csv")

new_employee_data = []
SSN=[]
SSN_Encrypt =[]
DOB=[]
DOB_format=[]
FirstName= []
LastName =[]

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}

# Read data into dictionary and create a new email field
with open(filepath) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
         FirstName = row["Name"].split()[0]
         LastName = row["Name"].split()[1]
         DOB = row["DOB"]
         for DOB_format in DOB:
            DOB_format =  datetime.datetime.strptime(DOB, '%Y-%m-%d').strftime('%-m/%d/%Y')  # This writes "06/24/1984"
         SSN = row["SSN"].split("-")[2]
         for SSN_Encrypt in SSN:
            SSN_Encrypt =("XXX-XXX-"+str(SSN))
         State= row["State"]
         for US_States_short in State:
             US_States_short=us_state_abbrev.get(row['State'])
         new_employee_data.append(
            {
                "First_name": FirstName,
                "Last_name": LastName,
                "DOB": DOB_format,
                "SSN": SSN_Encrypt,
                "State": US_States_short  
            }
        )
#Write updated data to csv file
csvpath = os.path.join("..","PyBoss","raw_data", "employees.csv")
with open(csvpath, "w") as csvfile:
    fieldnames = ["First_name", "Last_name", "DOB", "SSN", "State"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(new_employee_data)
