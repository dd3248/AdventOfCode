with open ("in") as f:
	lines=f.read().split('\n')

for i in range(len(lines)):
	lines[i] = lines[i].split(' ')
	lines[i][1] = lines[i][1].replace(':', '')
	lines[i][0] = lines[i][0].split('-')

valid=0
for line in lines:
	cnt=0
	for letter in line[2]:
		if letter == line[1]:
			cnt += 1

	if line[2][int(line[0][0])-1]==line[1]:
		if line[2][int(line[0][1])-1]!=line[1]:
			valid += 1

	if line[2][int(line[0][1])-1]==line[1]:
		if line[2][int(line[0][0])-1]!=line[1]:
			valid += 1
	
print(valid)