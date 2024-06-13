def bits2string(b=None):
    # Convert each 6-bit binary chunk to its decimal value, then to the corresponding character
    chars = []
    for x in b:
        if len(x) == 6:
            # Interpret the 6 bits as a character in the printable ASCII range
            chars.append(chr(int(x, 2)))
    return ''.join(chars)

def numberconverter(list):
    n = 0
    for i in range(0,6):
        if (list[i] == "1"):
            n = n + pow(2,5-i)
    return n


def number2string(number):
    if 0 <= number <= 25:
        return chr(number + ord('A'))
    if 26 <= number <= 51:
        return chr(number -26 + ord('a'))
    if 52 <= number <= 61:
        return chr(number -52 + ord('0'))
    if number == 62:
        return "+"
    if number == 63:
        return "/"


def encodedstring(list):
    encoded = []
    for i in range(0,len(list)):
        encoded.append(number2string(list[i]))
    code = ''.join(encoded)
    return code
    

def hexa2dezimal(list):
    n = list[0]*16 + list[1]
    return n



########################################################################




# Hex-Coded String
str = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
# Hex Decoded String
#str = "I'm killing your brain like a poisonous mushroom"

# Inputstring
#str = "49276d"

print("Hexastring:" + str)
print("-----------------------------------------")

# Umwandlung bytes
#data = str.encode('utf-8')

#Bitfolge als String
#bit_string = ''.join(format(byte, '08b') for byte in data) 


#print(bit_string)




#####################################################################


hexalist = ['a','b','c','d','e','f']

# In Characterpaare aufteilen
Characterlist = []
for i in range(0,len(str)):
    if i % 2 == 1:
        Characterlist.append([str[i-1], str[i]])
        
#print(Characterlist)

# Wandle von String in int um und schreibe a-e als 10-15
for i in range(0,int(len(str)/2)):
    for j in range(0,2):
        if Characterlist[i][j] == 'a':
            Characterlist[i][j] = int(10)
        if Characterlist[i][j] == 'b':
            Characterlist[i][j] = int(11)
        if Characterlist[i][j] == 'c':
            Characterlist[i][j] = int(12)
        if Characterlist[i][j] == 'd':
            Characterlist[i][j] = int(13)
        if Characterlist[i][j] == 'e':
            Characterlist[i][j] = int(14)
        if Characterlist[i][j] == 'f':
            Characterlist[i][j] = int(15)
        Characterlist[i][j] = int(Characterlist[i][j])


print("Schreibe Hexastring in Paare und ersetze Buchstaben mit jeweiligen Zahlen")
print(Characterlist)
print("-----------------------------------------")


# Für jeden Eintrag in Characterlist soll jetzt die Binärzahl 
# berechnet werden
seven_bit = []
for i in range(0,int(len(str)/2)):
    k = hexa2dezimal(Characterlist[i])
    b = bin(k)
    s = b.replace('0b','')
    seven_bit.append(s)
print("Hexadezimalinput in Binär")
print(seven_bit)    
print("-----------------------------------------")
print("Jede bitfolge muss jetzt auf ein byte geeicht werden")

for i in range(0, int(len(str)/2)):
    n = len(seven_bit[i])
    k = n % 8
    if k > 0:
        for j in range(0, 8-k):
            seven_bit[i] = "0" + seven_bit[i]
            
            
print(seven_bit)           





print("-----------------------------------------")


bit_string = ''    
for i in range(0, int(len(str)/2)):
    bit_string = bit_string + seven_bit[i]




# Leere Matrix zum späteren Speichern
Aufteilung = []

n = len(bit_string)
m = n % 3
t = len(bit_string)/6
f = int(t)

# Teile Bytes in 6 Bit Intervalle auf
if (m == 0):
    for i in range(0,f):
        zwischen = []
        for j in range(0,6):
            zwischen.append(bit_string[6*i+j])
        Aufteilung.append(zwischen)       
elif (m == 2):
    #str = str + "\x00" 
    #str = str + "\x00" 
    ## HIER IST DER FEHLER; ADDE NICHT AUF DEN STRING
    #data = str.encode('utf-8')
    #bit_string = ''.join(format(byte, '08b') for byte in data)     
#    t = len(bit_string)/6
#    f = int(t)

    print("Adde 2 Bytes")
    bit_string = bit_string + "0000000000000000"
    print(bit_string)
    
    t = len(bit_string)/6
    f = int(t)
    
    for i in range(0,f):
        zwischen = []
        for j in range(0,6):
            zwischen.append(bit_string[6*i+j])
        Aufteilung.append(zwischen)    
else:
    #str = str + "\x00"    
    ## HIER IST DER FEHLER; ADDE NUR BYTES 
    #data = str.encode('utf-8')
    #bit_string = ''.join(format(byte, '08b') for byte in data) 
    print("Adde einen Byte")
    bit_string = bit_string + "00000000"
    print(bit_string)
    t = len(bit_string)/6
    f = int(t)
    for i in range(0,f):
        zwischen = []
        for j in range(0,6):
            zwischen.append(bit_string[6*i+j])
        Aufteilung.append(zwischen)


print("-----------------------------------------")


print(Aufteilung)
    
    
    
# WANDLE JEDE 6-BIT-LISTE IN DEZIMALZAHLEN UM
base64list = []
for i in range(0,f):
    helplist =[]
    for j in range(0,6):
        helplist.append(Aufteilung[i][j])
    c = numberconverter(helplist)
    base64list.append(c)
tl = encodedstring(base64list)

   
    

# Je nachdem, wv Paddingbytes wird "=" ersetzt
if m > 0:
    tl = tl[:-m]
    liste = []
    for i in range(0,m):
        tl = tl + "="



print(tl)

