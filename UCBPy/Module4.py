longest=0
f = open('c:/Users/awinarsk/Desktop/Module4.py','r')
while 1:
    line = f.readline()
    if not line:
        break
    if len(line) > longest:
       longest=len(line)
       continue
print('Longest line is %(longest).d' % locals() )

