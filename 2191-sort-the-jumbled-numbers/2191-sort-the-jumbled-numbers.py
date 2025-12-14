class Solution:
    def sortJumbled(self, mapping: List[int], nums: List[int]) -> List[int]:
        store_pairs = []

        for i in range(len(nums)):
            number = str(nums[i])
            formed = ""
            for j in range(len(number)):
                formed = formed + str(mapping[int(number[j])])
            mapped_value = int(formed)
            store_pairs.append((mapped_value, i))
        store_pairs.sort()
        answer = []
        for pair in store_pairs:
            answer.append(nums[pair[1]])
        return answer
        # store_pairs=[]
        # for idx,num in enumerate(nums):
        #     integer_list=[int(i) for i in str(num)]
        #     new_num=""
        #     for i in integer_list:
        #         new_num+=str(mapping[i])
        #     mapped_val=int(new_num)
        #     store_pairs .append((new_num,idx))
        # store_pairs.sort()
        # res=[]
        # for pair in store_pairs:
        #     res.append(nums[pair[1]])
        # return res
            
         