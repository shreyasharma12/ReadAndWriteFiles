import csv

def main():

        infile = open("EmployeePay.csv",'r')

        employees_file = csv.reader(infile, delimiter=',')

        next(employees_file)

#to skip a line if the file contains a header record 

        outfile = open("Employee_Bonus.csv",'w')

        for record in employees_file:
                ID = record[0]
                FirstName = record[1]
                LastName = record[2]
                Salary = record[3]
                Bonus = record[4]
                TotalPay = float(record[3]) * (float(record[3]) * float(record[4]))
                
                outfile.write(ID + ',' + FirstName + ',' + LastName + ',' + Salary + ',' + Bonus + ',' + format(TotalPay) + "\n")

        infile.close()
        outfile.close()
main()
