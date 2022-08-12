from random import choice

#This is a stub function to flip bits
def bitFlip(x):
    if(x == '0'):
        return '1'
    return '0'

#Generates a random bit message
def genMsg(k):
    msg = ""
    for i in range (k):
        msg += choice(['0','1'])
    
    return msg

#This function computes XOR operator
def xor(a, b):
    c = ""
    for i in range(len(a)):
        if(a[i]==b[i]):
            c+='0'
        else:
            c+='1'
    return c

#This function is used to calculate division
def division(a, b):
    p = len(b)
    m = len(a)

    rem = a[0:p-1]
    for i in range(m-p+1):
        rem += a[i+p-1]
        if(rem[0]=='1'):
            rem = xor(rem, P)
            rem = rem[1:]
        else:
            rem = rem[1:]

    return rem

# This function is used to calculate CRC frame
def compFrame(msg, P):
    dividend = msg + ("0"*(len(P)-1))
    return msg + division(dividend, P)

#This function is used to insert error in the frame
def errorInsert(frame):
    err = ""
    rec = ""
    for i in range(len(frame)):
        if choice([True] + [False]*15):
            rec += bitFlip(frame[i])
            err += '1'
        else:
            rec += frame[i]
            err += '0'
    
    return rec, err
#This fuction is used to verify CRC
def fCheck(rec, P):
    remExp = "0"*(len(P)-1)

    if remExp== division(rec, P):
        return "Accept"
    return "Reject"

P = "110101"
k = 10
msg = genMsg(k)
frame = compFrame(msg, P)
rec, err = errorInsert(frame)
stat = fCheck(rec, P)

print("Input message: "+str(msg))
print("Sent CRC Frame: "+str(frame))
print("Error Pattern: "+str(err))
print("Received CRC Frame: "+str(rec))
print("Received Frame Status: "+str(stat))