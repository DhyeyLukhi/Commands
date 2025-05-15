class Solution:
    def Solution(self):
        pass

    def countzero(self, num1, num2):
        count = 0
        print("Into the counttozeor")

        while num1 != 0 and num2 != 0:
            
            if num1 >= num2:
                print("num1: ", num1)
                print("num2: ", num2)
                num1 = num1 - num2
                count = count + 1
            
            elif num1 <= num2:
                print("num1: ", num1)
                print("num2: ", num2)
                num2 = num2 - num1
                count = count + 1

        return count

if __name__ == '__main__':
    objc = Solution()
    value1 = int(input("Value 1: "))
    value2 = int(input("Value 2: "))
    ans = objc.countzero(value1, value2)
    print(ans)
