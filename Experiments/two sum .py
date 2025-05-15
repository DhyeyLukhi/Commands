class Solution:
    '''Here the function twoSum is defined
    It actually calculate the sum of first integer and the integers next to it in the array
    and if it gets the answer, it breaks the for loop and prints the answer.
    If it didn't get the answer then it again called the function and pass the same array
    but without the first element of the array'''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        bool = False
        for i in range(0, len(nums) - 1):
            if nums[0] + nums[i + 1] == target:
                print(f"Values: {nums[0]}, {nums[i+1]}")
                bool = True
                break
        if not bool:
            self.twoSum(nums[1:], target)



if __name__ == '__main__':
    solve = Solution()
    try: 
        target = int(input("Target: "))  # Ask the value for Target
        nums = int(input("List of numbers: "))  # Ask the number of vlaues to be inputted in array
        if (nums < 2):
            raise Exception("List of numbers must be greater than 1")
        list = mylist = []
        for i in range(0, int(nums)):
            value = int(input("Number: "))
            mylist.append(int(value))

        solve.twoSum(nums=mylist, target=target)  # Call the function of the class

    except Exception as e:
        print(e)