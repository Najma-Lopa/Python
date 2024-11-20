# write in file

with open('massage.txt','a') as fileWrite:
    fileWrite.write(' hello world')

#read from file
with open('massage.txt','r') as fileRead:
    text=fileRead.read()
    print(text)