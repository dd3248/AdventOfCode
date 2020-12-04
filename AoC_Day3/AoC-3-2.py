with open ("in") as f:
	lines=f.read().split('\n')

line_length=len(lines[0])
num_rows=len(lines)
tree_cnts=[]

slopes = [[1,1],[3,1],[5,1],[7,1],[1,2]]

for slope in slopes:
	tree_cnt=0
	row=0
	col=0
	while row < num_rows:
		if lines[row][col] == '#':
			tree_cnt += 1
		
		row+=slope[1]
		col+=slope[0]
		if col >= line_length-1:
			col = col % line_length

	tree_cnts.append(tree_cnt)

mult=1
for val in tree_cnts:
	mult*=val

print(mult)