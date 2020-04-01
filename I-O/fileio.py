#jabber = open("/home/kline/Dev/Python-Mastery/I-O/sample.txt", 'r') #<--full path
#jabber = open("sample.txt", 'r')

#for line in jabber:
#     print(line)
#jabber.close()
"""using the with statement allows the .close() to not be nessecary because it is
then assigned to memory for a dump when the loop fails or there is an error.  this
is usefull for error handling just in case something were to happen to your file
and you don't have an error handler"""
with open("sample.txt", 'r') as jabber:
    for i in jabber:
        if "JAB" in i.upper():
            print(i, end = '')
print("-"*80)
with open("sample.txt", 'r')as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()
