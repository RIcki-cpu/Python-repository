"""
8.4 Open the file romeo.txt and read it line by line. For each line,
split the line into a list of words using the split() method.
The program should build a list of words. For each word on each line check to see
if the word is already in the list and if not append it to the list. When the program completes,
sort and print the resulting words in alphabetical order.
"""
name=input("Enter file name: ")
romeo=open(name)
list0=list()
for line in romeo:
    list1=line.split()
    for word in list1:
        if word in list0: continue
        list0.append(word)
list0.sort()
print(list0)
