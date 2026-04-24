import sys
def minimum_of_arr(arr,ans):
    if len(arr)==0:
        print(ans)
        return 
    ans = min(arr[0],ans)
    minimum_of_arr(arr[1:],ans)
arr = [1,2,3,4,0]
minimum_of_arr(arr,sys.maxsize)