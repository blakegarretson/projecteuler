names = {
    "0":"",
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "10":"ten",
    "11":"eleven",
    "12":"twelve",
    "13":"thirteen",
    "14":"fourteen",
    "15":"fifteen",
    "16":"sixteen",
    "17":"seventeen",
    "18":"eighteen",
    "19":"nineteen"
    }
names_tens = {    
    "2":"twenty",
    "3":"thirty",
    "4":"forty",
    "5":"fifty",
    "6":"sixty",
    "7":"seventy",
    "8":"eighty",
    "9":"ninety",
    }
    
total_letters = 0
  
for x in range(1,1001):
    s = str(x)
    namestr = ""
    if len(s) == 4:
        namestr += "one thousand "
        s = s[1:]
    if len(s) == 3:
        if s[0] != "0":
            namestr += names[s[0]]+" hundred "
            if s[1:].replace("0",""):
                namestr += "and "
        s = s[1:]
    if len(s) == 2:
        if s[0] == '1':
            namestr += names[s]
            s = ""
        else:
            if s[0] != "0":
                namestr += names_tens[s[0]] + " "
            s = s[1:]
    if len(s) == 1:
        if s[0] != "0":
            namestr += names[s]
    print namestr    
    total_letters += len(namestr.replace(" ",""))
    
print total_letters