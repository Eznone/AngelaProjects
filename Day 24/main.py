#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

from newFile import NewFile
from mail import Mail
newF = NewFile()

lNames = newF.retrieveLNames()
letterC = newF.retrieveLetterContents()

#Tests to see if the lNames and letterC work properly
#print(lNames)
#print(letterC)

mailFun = Mail()

mailFun.send_mail(lNames, letterC)

