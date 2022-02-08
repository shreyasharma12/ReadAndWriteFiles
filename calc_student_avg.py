   
import csv

def main():

    infile = open("Student_Scores.csv",'r')

    student_file = csv.reader(infile, delimiter = ',')

    outfile = open("student_avg.csv",'w')

    for record in student_file:
       FirstName = record[0]
       Grade1 = record[1]
       Grade2 = record[2]
       Grade3 = record[3]
       avg = (float(record[1]) + float(record[2]) + float(record[3]))/3
       outfile.write(FirstName + "," + format(round(avg,2)) + "\n") 
    
    infile.close()
    outfile.close()
    
main()