import xlsxwriter #Importing our library
import math
your_workbook = xlsxwriter.Workbook('./hello_world_xlwt.xlsx')  #Creating the workbook
sheet1 = your_workbook.add_worksheet('Sheet 1')  #The add.worksheet() helps you add a worksheet into your excel files
row = 0
for Zombie in range(12):
    for Cone in range(7):
        for Bungee in range(5):
            for Ladder in range(4):
                for Bucket in range(5):
                    for Jack in range(4):
                        for Cata in range(3):
                            if(Zombie+2*Cone+3*Bungee+4*Ladder+4*Bucket+3*Jack+5*Cata > 11):
                                continue
                            for j in range((int)(math.factorial(Zombie+Cone+Bungee+Ladder+Bucket+Jack+Cata)/math.factorial(Zombie)/math.factorial(Cone)/math.factorial(Bungee)/math.factorial(Ladder)/math.factorial(Bucket)/math.factorial(Jack)/math.factorial(Cata))):
                                sheet1.write(row, 0, Cata)
                                sheet1.write(row, 1, Zombie)
                                sheet1.write(row, 2, Cone)
                                sheet1.write(row, 3, Bungee)
                                sheet1.write(row, 4, Ladder)
                                sheet1.write(row, 5, Bucket)
                                sheet1.write(row, 6, Jack)
                                row += 1
your_workbook.close()
