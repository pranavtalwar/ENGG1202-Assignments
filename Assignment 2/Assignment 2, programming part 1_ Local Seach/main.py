from nqueen import *
import itertools
all_states=list(itertools.permutations((0,1,2,3,4)))
win1=0
win2=0
times_move_equal=0
moves_for_one=0 
moves_for_two=0
total_cases=0
one_fail=0 
two_fail=0  
both_fail=0
for i in range(len(all_states)):
    if(localSearch(all_states[i])=='a'):
        if(localSearch2(all_states[i])=='a'):
            both_fail+=1
        else:
            one_fail+=1
    elif(localSearch2(all_states[i])=='a'):
        two_fail+=1
    else:
        total_cases+=1
        local1count=localSearch(all_states[i])
        local2count=localSearch2(all_states[i])
        moves_for_one += local1count
        moves_for_two += local2count
        if(local1count>local2count):
            win2+=1
        elif(local1count<local2count):
            win1+=1
        else:
            times_move_equal+=1

print("localSearch() winning in less moves:",win1)
print("localSearch2() winning in less moves:",win2)
print("Ties:",times_move_equal) 

print("Average Moves for Move 1: ",moves_for_one/total_cases)
print("Average Moves for Move 2: ",moves_for_two/total_cases)

print("Number of times localSearch() does not solve the problem:",one_fail)
print("Number of times localSearch2() does not solve the problem:",two_fail)
print("Number of times both of them do not solve the problem:",both_fail)