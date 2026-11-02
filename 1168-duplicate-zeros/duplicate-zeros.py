class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count=0
        for num in arr:
            if  num==0:
                count+=1
        i=len(arr)-1
        j=len(arr)+count-1

        while i>=0:

            if arr[i]==0:
                if j<len(arr):
                    arr[j]=0
                j-=1
                if j<len(arr):
                    arr[j]=0
                j-=1
            else:
                if j <len(arr):
                    arr[j]=arr[i]
                j-=1
            i-=1
                
            



        