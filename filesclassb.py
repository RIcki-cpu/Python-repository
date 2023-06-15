# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
value = 0.0
counter = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:") :
        a = line.find("0.")
        b = line.find(" ",a)
        snumber = line[a:b]
        valuex =float(snumber)
        value = value + valuex
        counter =  counter + 1
#average part
result=value/counter
print("Average spam confidence:",result)
