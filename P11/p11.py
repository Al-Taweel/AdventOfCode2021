
file1 = open('input.txt', 'r')
Lines = file1.readlines()
lanternfishs = [int(a) for a in str(Lines[0]).split(',')]

for day in range(1,81):
    for fish in range(len(lanternfishs)):
        if lanternfishs[fish] == 0:
            lanternfishs.append(8)
            lanternfishs[fish] = 6
        else:
            lanternfishs[fish] -= 1 
    print('Day:'+str(day)+'\n')
    print('length='+str(len(lanternfishs))+'\n')
print(len(lanternfishs))