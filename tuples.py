"""
10.2 Write a program to read through the mbox-short.txt and figure out the distribution
 by hour of the day for each of the messages.
You can pull the hour out from the 'From ' line by finding the time and then splitting the
string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.
"""
name = input("Enter file name: ")
mbox = open(name)
dic1 = {}

for line in mbox :
    l1=line.split() # split each line of the txt
    if len(l1) < 3 or l1[0]!="From" : continue
    l2 = l1[5].split(":")# split the hour in hour/minutes/seconds
    hour = l2[0]
    dic1[hour]=dic1.get(hour,0) + 1 # adds one element to the diccionary even if it doesn't exists

#print(dic1.items())
# This part prints the diccionary sorted
for k,v in sorted(dic1.items()):
    print(k,v)
