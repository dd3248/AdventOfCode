with open("in") as f:
	groups=f.read().split('\n\n')

total=0

for group in groups:
	valid=0
	for key in ['byr:','iyr:','eyr:','hgt:','hcl:','ecl:','pid:']:
		if key in group:
			valid+=1
		if valid==7:
			total+=1

print(total)