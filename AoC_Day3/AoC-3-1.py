with open ("in") as f:
	lines=f.read().split('\n')

tree_cnt=0
row=0
col=0
line_length=len(lines[0])
num_rows=len(lines)

while row < num_rows:
	if lines[row][col] == '#':
		tree_cnt += 1
	
	row+=1
	col+=3
	if col >= line_length-1:
		col = col % line_length

print(tree_cnt)