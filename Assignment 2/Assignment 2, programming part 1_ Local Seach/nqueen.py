def countAttack(queen):
    count = 0
    for row1 in range( 0, len(queen) ):
        for row2 in range( row1 + 1, len( queen ) ):
            if queen[row1] == queen[row2]:
                count += 1
            elif abs(queen[row1] - queen[row2]) == (row2 - row1):
                count += 1      
    return count
def printBoard(queen):
  for n in queen:
    print("- "*n+"Q"+" -"*(len(queen)-n-1))
def printMatrix(queen):
    queen=list(queen)
    for i in range(0,len(queen)):
        k=queen[i]
        for j in range(0,len(queen)):
            if(j==k):
                print("{:<2}".format("-"), end=" ")
            else:
                queen[i]=j
                print("{:<2}".format(countAttack(queen)), end=" ")
        queen[i]=k
        print()
def moveOne(queen):
    check=0
    queen2=()
    min=countAttack(queen)
    queen=list(queen)
    for i in range(0,len(queen)):
        k=queen[i]
        for j in range(0,len(queen)):
            if(j!=k):
                queen[i]=j
                if(countAttack(queen)<=min):
                    queen2=tuple(queen)
                    min=countAttack(queen)
                    check=1
        queen[i]=k
    if(check==0):
        max=(len(queen)*(len(queen)-1))//2
        for i in range(0,len(queen)):
            k=queen[i]
            for j in range(0,len(queen)):
                if(j!=k):
                    queen[i]=j
                    if(countAttack(queen)>min):
                        if(countAttack(queen)<max):
                            queen2=tuple(queen)
                            max=countAttack(queen)
            queen[i]=k
    return queen2
def printMatrix2(queen):
    queen=list(queen)
    for i in range(0,len(queen)):
        for j in range(0,len(queen)):
            if(j==i):
                print("{:<2}".format("-"), end=" ")
            else:
                queen[i],queen[j]=queen[j],queen[i]
                print("{:<2}".format(countAttack(queen)), end=" ")
                queen[j],queen[i]=queen[i], queen[j]
        print()
def moveTwo(queen):
    check=0
    queen2=()
    min=countAttack(queen)
    queen=list(queen)
    for i in range(0,len(queen)):
        for j in range(0,len(queen)):
            if(j!=i):
                queen[i], queen[j]=queen[j], queen[i]
                if(countAttack(tuple(queen))<=min):
                    queen2=tuple(queen)
                    min=countAttack(queen)
                    check=1
                queen[j], queen[i]=queen[i], queen[j]
    if(check==0):
        max=(len(queen)*(len(queen)-1))//2
        for i in range(0,len(queen)):
            for j in range(0,len(queen)):
                if(j!=i):
                    queen[i], queen[j]=queen[j], queen[i]
                    if(countAttack(tuple(queen))>min):
                        if(countAttack(queen)<max):
                            queen2=tuple(queen)
                            max=countAttack(queen)
                    queen[j], queen[i]=queen[i], queen[j]
    return queen2
def localSearch(queen):
    count=0
    while countAttack(queen) >0:
        queen=moveOne(queen)
        count+=1
        if count>100:
            return 'a'
    return count


def localSearch2(queen):
  count=0  
  while countAttack(queen) > 0:
    queen = moveTwo(queen)
    count +=1
    if count>100:
        return 'a'
  return count

