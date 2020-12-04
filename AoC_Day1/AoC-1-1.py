with open('in') as f:
	nums=[int(item) for item in f.read().split('\n')]

nums.sort()

def find_2020_sum(nums):
	first=0
	last=len(nums)-1

	while True:
		if nums[first]+nums[last] > 2020:
			last-=1
		elif nums[first]+nums[last] < 2020:
			first+=1
		elif nums[first]+nums[last] == 2020:
			return nums[first]*nums[last]

	return None

sol=find_2020_sum(nums)

print(sol)