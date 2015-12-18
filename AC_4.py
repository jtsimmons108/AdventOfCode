import md5

for num in range(10**6,10**7):
    if md5.new('ckczppom'+str(num)).hexdigest()[0:6] == '000000':
        print num
        break