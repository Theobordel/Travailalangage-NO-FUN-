conerie = 1000^4
mon_tab = [1,0,0,0]

test = [0,0,1]

if test[0] in mon_tab:
    print(mon_tab,test)
else:
    print("toto")



with open('geeks.txt','w') as file_reader:
    file_reader.write("GeeksforGeeks")
print("File before removing the last character",open('geeks.txt').read())
with open('geeks.txt', 'rb+') as fh:
    fh.seek(-1, 2)
    fh.truncate()
print("File after removing the last character",open('geeks.txt').read())