# Inwk6312-Winter2018-ProgrammingTask3

# Programming Task 3

  - You have to clone this repo to your account, you should be seeing this on your account, if someone elses name is listed call an instructor for help.
  - Use the Ubuntu VM to write the progrm.
  - Use git add, commit and push to send the code back. 
  - Don't forget to add user name and email on git. 
  - You are allowed to use any form of searching and documentation reading and book reading is promoted
  - You cannot talk to your other people or ask for help!

# Halifax Open Data

You are given a csv file from [Halifax's open data](https://www.halifax.ca/home/open-data). 

  - The file is a csv (comma seperated values); i.e, it's like a excel spreadsheet but simple
  - You can read the file without modification to it.
  - You are asked to extract some information from it. 

### Bus Routes

The CSV you are given has details of the Point representation of bus stop locations which occur along roadways, terminals and park and ride facilities in HRM. Includes information on the type of bus stop and stop number.  This is a point dataset that has been derived from the source data in Hastus (Halifax Transit system).

This is the origianl source  -> https://catalogue-hrm.opendata.arcgis.com/datasets/bus-stops

### Task - Output formatting

You need to print a list that has a solution like this (Do not print all the data):

| Stop Number | Location | FCODE |
| ------ | ------ |------ |
| 6123 | Barrington St Before Spring Garden Rd (6123) |Conventional Transit Bus Stop |
| 9110 | Lacewood Terminal Bay 10 (9110) |Terminal |

## Create a different python file for each task with the format task#.py (where # = task number!)

### Task - 1

Total number of Terminals (FCODE = Terminal)
Total number of Bus Stops (FCODE = Terminal)
Print list of terminals that have accessible (ACCESSIBLE = Accessible)
Print list of terminals that are not accessible (ACCESSIBLE = Inaccessible)
(Ignore Non-standard.)

### Task - 2

Get correct street name from the user as a string. 
Print list of all stops on that street in the above format. 

### Development

Use with open to open file:
```py
with open(file, 'r') as myfile
```
Use string functions to seperate the values and extract the interesting value to a data structure of your choice!


License
----

MIT
https://www.halifax.ca/home/open-data/open-data-license

