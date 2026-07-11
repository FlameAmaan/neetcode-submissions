class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start,end=0,len(matrix)-1
        while start<=end:
            mid=(start+end)//2
            if target==matrix[mid][0]:
                return True
            if target>=matrix[mid][0] and target<=matrix[mid][len(matrix[0])-1]:
                if self.binarySearch(matrix[mid],target):
                    return True
                return False
            if target<matrix[mid][0]:
                end=mid-1
            else:
                start=mid+1
        return False




    def binarySearch(self,arr,target):
        start,end=0,len(arr)-1
        while start<=end:
            mid=(start+end)//2
            if arr[mid]==target:
                return True
            if arr[mid]>target:
                end=mid-1
            else:
                start=mid+1
        return False