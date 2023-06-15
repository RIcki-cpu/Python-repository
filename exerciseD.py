"""
9.4 Write a program to read through the mbox-short.txt and figure out who has sent the greatest number of mail messages.
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail.
The program creates a Python dictionary that maps the sender's mail address to a count of the number of
times they appear in the file. After the dictionary is produced, the program reads through the dictionary
using a maximum loop to find the most prolific committer.
"""
dic1 = {} # This is an empty diccionary
name = input("Enter file name: ")
mbox = open(name)
for line in mbox :
    l1=line.split()
    if len(l1) < 3 or l1[0]!="From" : continue
    mail=l1[1] # This part saves the email
    dic1[mail] = dic1.get(mail,0)+1

#print(dic1.items()) # This prints the diccionary
#This part calculate the largest ocurrence of an email

maxc = 0
email = None
for pss,val in dic1.items() :
    if val>maxc :
        maxc = val
        email= pss
print(email," ",maxc)
