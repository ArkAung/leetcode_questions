[Answer on LeetCode](https://leetcode.com/problems/jump-game/discuss/596454/python-simple-solution-with-thinking-process-runtime-on/524515)

When I first see this problem, two things pop up in my mind:
* Maybe I can do some sort of DFS, BFS (with backtracking?) but there will be a lot of redundancies
* Then this begs for Dynamic Programming!

But my gut feeling was saying that this problem has to have a simpler approach.

So, here is my thinking process:
* Base case: last index can trivially reach to last index.
* **Q1**: How can I reach to the last index (I will call it `last_position`) from a preceding index?
	* If I have a preceding index `idx` in `nums` which has jump count `jump` which satisfies `idx+jump >= last_position`, I know that this `idx` is good enough to be treated as the last index because all I need to do now is to get to that `idx`. I am going to treat this new `idx` as a new `last_position`.
* I ask **Q1** again.

So now, here are two important things:
* If we have indices which are like **sinkholes**, those with 0 as jump and every other preceding index can only jump to that sinkhole, our `last_position` will not be updated anymore because `idx+jump >= last_position` will not be satisfied at that sinkhole and every other preceding index cannot satisfy the `idx+jump >= last_position` condition since their jumps are not big enough.
E.g. ```nums=[3,2,1,0,4] # Here 0 is a sinkhole becuase all preceding indices can only jump to the sinkhole```
* If we have **barriers**, those indices with 0 as jump, but the preceding indices contain jumps which can go beyond those barriers, `idx+jump >= last_position` will be satisfied and `last_position` will be updated.
E.g. ```nums=[3,2,2,0,4] # Here 0 is just a barrier since the index before that 0 can jump *over* that barrier```

Finally ask this question when we have finished looping
* Is the last position index of 0? (i.e, have we reached to the beginning while doing the process of jumping and updating the `last_position`?)
* If we have sinkholes in `nums`, our `last_position` will not be 0. Thus, `False` will be retured.

That's all!

This is what I have in mind when I was thinking of this approach :D
![image](https://assets.leetcode.com/users/arkaung/image_1587809403.png)

## Python
``` python
1. class Solution:
2.    def canJump(self, nums: List[int]) -> bool:
3.        last_position = len(nums)-1
4.        
5.        for i in range(len(nums)-2,-1,-1): # Iterate backwards from second to last item until the first item
6.            if (i + nums[i]) >= last_position: # If this index has jump count which can reach to or beyond the last position
7.                last_position = i # Since we just need to reach to this new index
8.        return last_position == 0	
```

But during the interview, this approach may not be apparent or maybe the interviewer is looking for something. 

