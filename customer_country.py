import csv

infile = open("customers.csv",'r')

customer_file = csv.reader(infile, delimiter=',')

#to skip a line if the file contains a header record 
next(customer_file)

outfile = open("customer_country.csv", 'w')

for record in customer_file:
        FirstName = record[1]
        LastName = record[2]
        Country = record[4]
        outfile.write(FirstName + ',' + record[2] + ',' + record[4] + '\n')


