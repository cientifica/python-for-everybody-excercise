mail=open('mbox-short.txt')
total=0
count=0
for line in mail:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    line=line.rstrip()
    line=line.split()
    n=float(line[1])
    print(n)
    total+=n
    count+=1
average=total/count
print('Average spam confidence:',average)
        