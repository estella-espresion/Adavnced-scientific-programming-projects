#Filename: hw_payroll.py
#Pupose: This program will calculate and process employees and their pay.

print("Hello! This program will help you process your employees' weekly salary. \n\n")

a = 0 #loop control variable
while a < 1: #Main loop to process each employee
    print("To get started, please enter your employee's name. \n\n")
    employeeName = str(input())

    print("\nPlease enter ", employeeName, "'s hourly pay rate. \n\n")
    hourlyRate = float(input())

    print("\nEnter the number of hours ", employeeName, " worked per day over the work-week. \n")

    b = 1
    totalHours = 0

    while b < 6: #loop to process employee's daily hours
        print("\n For Day ", b, ": \n\n")
        hoursWorked = int(input())

        if hoursWorked < 0: #loop to validate user input
            print("You have entered an invalid amount. Please try again.")
            hoursWorked = 0
            b = b - 1 #allows the user to input the day's hours again
        elif hoursWorked > 24:
            print("You have entered an invalid amount. Please try again. ")
            hoursWorked = 0
            b = b - 1
        totalHours = totalHours + hoursWorked
        b = b + 1

    #Calculations:
    grossPay = hourlyRate * totalHours
    stateTax = grossPay * 0.0307
    ficaTax = grossPay * 0.0886
    if grossPay < 5000: #calculates the federal tax
        federalTax = grossPay * 0.15
    elif grossPay >= 5000:
        federalTax = grossPay * 0.25
    witholdingAmt = stateTax + ficaTax + federalTax
    netPay = grossPay - witholdingAmt

    #Print Results
    print(employeeName, "'s weekly salary report: \n\n")
    print("Employee Name : ", employeeName, "\n")
    print("Gross Pay : $", "{0:.2f}".format(grossPay), "\n")
    print("Total Witholding Amount : $", "{0:.2f}".format(witholdingAmt), "\n")
    print("Net Pay : $", "{0:.2f}".format(netPay))

    print("\nWould you like to process another employee?")
    print("If so, enter 'yes' or enter 'done' to terminate the program")

    answer = str(input())

    if answer == "done": #closing the program
        print("\n Thank you for using this program. Have a good day! \n")
        a = a + 1
    elif answer == "Done":
        print("\n Thank you for using this program. Have a good day! \n")
        a = a + 1
