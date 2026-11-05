paisA = 90000000
paisB = 140000000
anos = 0
while paisB > paisA:
    paisA += ((paisA * 3.5) / 100)
    paisB += (paisB / 100)
    anos += 1
print (anos , "anos")
