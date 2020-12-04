with open('in') as f:
	nums=[int(item) for item in f.read().split('\n')]

nums.sort()

def find_2020_sum3(nums):
	first=0
	last=len(nums)-1

	for i in nums:
		while True:
			if nums[first]+nums[last]+i > 2020:
				last-=1
			elif nums[first]+nums[last]+i < 2020:
				first+=1
			elif nums[first]+nums[last]+i == 2020:
				return nums[first]*nums[last]*i

	return None

sol=find_2020_sum3(nums)

print(sol)