import os
import sys #used for converting the byte to decimal

byte0=0
byte1=0
byte2=0
byte3=0
byte4=0
byte5=0

xdifference=0
ydifference=0

loop=0

hypotlist=[] #sets the list to zero, hard reset

filename = input('file: ') #runs the user prompt for selecting the file
f=open(filename, 'rb') #opens the file as a binary

with open(filename, "rb") as binary_file: #maybe redundant?
    file_size = os.path.getsize(filename) #gets the filesize
    if (file_size % 2) == 0: #if file size is divisible by two
        divisible=1
    else:
        divisible=0
    f.seek(file_size-1)
    fff=(f.read(1))
    #print((int.from_bytes(fff, byteorder=sys.byteorder))) #reads the last byte
    f.seek(0)
    ggg=(f.read(1))
    #print((int.from_bytes(ggg, byteorder=sys.byteorder))) #reads the first byte
    if ((int.from_bytes(ggg, byteorder=sys.byteorder))) == (int.from_bytes(fff, byteorder=sys.byteorder)): #if last byte is the same as the first byte
        loops=1
    else:
        loops=0
    f.seek(0)


    while loop <= (file_size/6):
        piece = f.read(1)
        byte0=(int.from_bytes(piece, byteorder=sys.byteorder))
        #print(byte0)
        piece = f.read(1)
        byte1=(int.from_bytes(piece, byteorder=sys.byteorder))
        #print(byte1)
        piece = f.read(1)
        byte2=(int.from_bytes(piece, byteorder=sys.byteorder))
        #print(byte2)
        piece = f.read(1)
        byte3=(int.from_bytes(piece, byteorder=sys.byteorder))
        #print(byte3)

        legnth=((((byte3-byte1)**2)+((byte2-byte0)**2))**0.5)
        #print(legnth)
        hypotlist.append(legnth)

        byte0=byte2
        byte1=byte3

        piece = f.read(1)
        byte2=(int.from_bytes(piece, byteorder=sys.byteorder))
        #print(byte2)
        piece = f.read(1)
        byte3=(int.from_bytes(piece, byteorder=sys.byteorder))
        #print(byte3)

        legnth=((((byte3-byte1)**2)+((byte2-byte0)**2))**0.5)
        #print(legnth)
        hypotlist.append(legnth)

        loop += 1

        distance=(max(hypotlist))
        
print(hypotlist)
print(distance)
#print(file_size)
#print(divisible)
#print(loops)