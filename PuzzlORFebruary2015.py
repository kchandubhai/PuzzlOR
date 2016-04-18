#generate first set of coins
output = []
coinOption = [1,5,10,20]
for i in coinOption:
    for j in coinOption:
        for k in coinOption:
            for l in coinOption:
                for m in coinOption:
                    if i + j + k == 11 and i + l + m == 21:
                        output.append([i,j,k,l,m])


print(output)
