#Task 
#problem 1
# data=eval(input("Put Your list : "))

# def choose_number (list1) :
#     first_max=max(list1[0],list1[1])
#     seocnd_max=min(list1[0],list1[1])

#     for i in range (2,len(list1)):
#         if list1[1]>first_max :
#             seocnd_max =first_max
#             first_max= list1[1]

#         elif list1[1] > seocnd_max and first_max !=list1[1] :
#             seocnd_max=list1[1]

#     return seocnd_max 

# print ("Second largest number = " , choose_number(data))       

  


#problem 2

# list=[1,2,3,5,7,9]

# def get_missing (list):
#    out_put=[]
#    for i in range (1,11) :
#        if not i  in list  :
#            out_put.append(i)
#        return out_put


#problem 3


# def find_missing_number(nums):
#     n = len(nums) + 1 
    
#     xor_total = 0
#     for i in range(1, n + 1):
#         xor_total ^= i
    
#     xor_list = 0
#     for num in nums:
#         xor_list ^= num
    
   
#     missing_number = xor_total ^ xor_list
    
#     return missing_number


#problem 4


def find_rotation_count(nums):
    start, end = 0, len(nums) - 1
    n = len(nums)
    
    while start < end:
        mid = start + (end - start) // 2
        
       
        if mid > 0 and nums[mid] < nums[mid - 1]:
            return mid

        if nums[mid] > nums[end]:
            start = mid + 1
        else:
            end = mid
    
   
    return start


nums = [4, 5, 6, 7, 0, 1, 2]
rotation_count = find_rotation_count(nums)
print(f"The array has been rotated {rotation_count} times.")


  


         
