with open("in") as f:
	groups=f.read().split('\n\n')

for i in range(len(groups)):
	groups[i] = groups[i].replace('\n',' ')
	groups[i] = groups[i].split(' ')

total = 0

for group in groups:
	valid=0
	for tok in group:
		key=tok[:3]
		val=tok[4:]
		
		if key == 'byr':
			valid += 1 if (len(val)==4 and val.isdigit()) and (int(val) >= 1920 and int(val) <= 2002) else 0

		if key == 'iyr':
			valid += 1 if (len(val)==4 and val.isdigit()) and (int(val) >= 2010 and int(val) <= 2020) else 0

		if key == 'eyr':
			valid += 1 if (int(val) >= 2020 and int(val) <= 2030) else 0

		if key == 'hgt':
			if (val[-2:] == 'cm') and (int(val[:-2]) >= 150 and int(val[:-2]) <= 193):
				valid += 1
			elif (val[-2:] == 'in') and (int(val[:-2]) >= 59 and int(val[:-2]) <= 76):
				valid += 1

		if key == 'hcl':
			if val[0]=='#' and len(val)==7 and all([char in '0123456789abcdef' for char in val[1:]]):
				valid += 1

		if key == 'ecl':
			if len(val) == 3 and val in ['amb','blu','brn','gry','grn','hzl','oth']:
				valid += 1

		if key == 'pid':
			if len(val)==9 and val.isdigit():
				valid += 1

	if valid==7:
		total += 1

print(total)
