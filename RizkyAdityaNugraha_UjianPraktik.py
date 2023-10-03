#----------------------------------------------------#
# Nama      : Rizky Aditya Nugraha
# Matkul    : Teknologi Informasi
# Semester  : 1
# NPM       : 225540100200
# Tugas     : Ujian Praktik 1
#----------------------------------------------------#

#----------------------------------------------------#
#-----------Declare your function here---------------#
#----------------------------------------------------#

#1 
def minimalmaksimal(numlist):
    
    print("Your numbers is:",numlist)
    
    def smallnumber():
        tempnumbersmall = numlist[0]
        for i in range (len(numlist)):
            if numlist[i] < tempnumbersmall:
                tempnumbersmall = numlist[i]
            else:
                pass
        print("Smallest number is: ")
        print(tempnumbersmall,'\n')

    def beegnumber():
        tempnumberbeeg = numlist[0]
        for i in range (len(numlist)):
            if numlist[i] > tempnumberbeeg:
                tempnumberbeeg = numlist[i]
            else:
                pass
        print("Biggest number is: ")
        print(tempnumberbeeg,'\n')
        
    smallnumber()
    beegnumber()
    
#2
def anotherfactorial(number):
    anothernumber = 1
    for i in range(1,number+1):
        anothernumber = anothernumber * i
    print("The result of factorial number from", number,"is :")
    print(anothernumber,'\n')


def countwords(char, target):
    targetchar = []
    for i in char:
        if i == target:
            targetchar.append(i)
        else:
            pass
    targetedlength = len(targetchar)
    #print(targetchar)
    print("Your words is: ->",char, "<-and your count target is :",target)
    print("There's total",targetedlength,"letters in your targeted words",'\n')

#----------------------------------------------------#
#---------------End of your function-----------------#
#----------------------------------------------------#

#----------------------------------------------------#
#--------------Start of your program-----------------#
#----------------------------------------------------#

#1
numberlist = [438,234,857,349,128,914]
minimalmaksimal(numberlist)

#2
anotherfactorial(5)

#3
mywords = "aku adalah anak bapak budi"
countwords(mywords,"a")

#----------------------------------------------------#
#---------------End of your program------------------#
#----------------------------------------------------#
