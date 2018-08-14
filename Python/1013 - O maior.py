nums = str(input()).split()
nums2 = [0,0,0]
nums2[0],nums2[1],nums2[2] = int(nums[0]),int(nums[1]),int(nums[2])
nums2.sort()
maior = int(nums2[2])
print('{} eh o maior'.format(maior))
