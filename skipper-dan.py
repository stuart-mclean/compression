import os #used for getting the filesize
import sys #used for converting the byte to decimal
i = 0 #the variable used to reset the list
j = 0 #the variable used to write the data to the list
thislist = [] #sets the list to zero, hard reset
#read file
filename = input('file: ') #runs the user prompt for selecting the file
f=open(filename, 'rb') #opens the file as a binary
#get file size
with open(filename, "rb") as binary_file: #maybe redundant?
    file_size = os.path.getsize(filename) #gets the filesize
print(file_size) #write the filesize for verification and fun
print(filename) #prints the name for the file, just for clarity
#establishes list

while j < 256: #255 didn't work and 256 did.
    thislist.append(00) #fills the list with 256 blank zeroes
    j += 1 #repeat until 256 times repeated
#print(thislist)#gets the filesize
#establishes list
dumpfile = open(r"dump.txt", "w") #opens the dump file as write-only
dumpfile.write("") #write nothing
dumpfile.close() #close the file

while j < 256: #255 didn't work and 256 did.
    thislist.append(00) #fills the list with 256 blank zeroes
    j += 1 #repeat until 256 times repeated
#print(thislist)
dumpfile = open(r"dump.txt", "a")
with open(filename, "rb") as binary_file:
    contents = binary_file.read()
    while i < file_size: #the earlier established number of bytes does this repeat
    #take the current byte:
        piece = f.read(1) #read one byte
        locator=(int.from_bytes(piece, byteorder=sys.byteorder)) #figure out what this actually does, converts the raw byte to decimal
        #print(locator)
        thislist[locator] = thislist[locator] + 1 #add 1 to the corresponding tally on the list
        dumpfile.write(str(locator))
        dumpfile.write(" ")
        if i == (round(file_size*0.2)): #this is repeating, please fix this
            print("20% finished")
        if i == (round(file_size*0.4)):
            print("40% finished")
        if i == (round(file_size*0.6)):
            print("60% finished")
        if i == (round(file_size*0.8)):
            print("80% finished")
        i += 1 #repeat until finished
print(thislist) #outputs all the tallies
print("Most frquent decimal appears", max(thislist), "times.") #human-readable printing of the most frequent byte
dumpfile.close()
f.close()

#verify file size
#
#