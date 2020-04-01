"""make a times table for the number 2 featuring 1*2-12*2.  then, append said
table to the end of the jaborwalky text in sample.txt without breaking it."""
times_tables = []
with open("sample.txt", 'a')as ifile:
    for i in range(0, 13):
        times_tables.append("{} times 2 is {}".format(i, i*2))
