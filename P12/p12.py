
def create_initial_lanternfish_set(Lines):
    initial_set = [int(a) for a in str(Lines[0]).split(',')]
    lanternfishs = [0,0,0,0,0,0,0,0,0]
    for fish in initial_set:
        lanternfishs[fish] += 1
    return lanternfishs 

file1 = open('input.txt', 'r')
Lines = file1.readlines()

lanternfishs = create_initial_lanternfish_set(Lines)
for day in range(1,257):
    temp = lanternfishs[0] # Those need to spawn & go to lanternfishes[6] tomorrow
    for i in range(1,len(lanternfishs)):
        lanternfishs[i-1] = lanternfishs[i]
    lanternfishs[6] += temp
    lanternfishs[8] = temp

    print('Day:'+str(day)+'\n')
sum = 0
for n in lanternfishs:
    sum += n
print(sum)
