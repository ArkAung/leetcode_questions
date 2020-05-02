[Answer on LeetCode](https://leetcode.com/problems/decode-ways/discuss/608268/Python-Thinking-process-diagram-(DP-%2B-DFS))

First, I build a tree of possible decodings I can do from a random string.
* The number of leaves in the tree essentially is the number of ways the string can be decoded.
* We are going to build our tree with DFS from our original string, trying to decode either as:
	* A single digit (and call dfs again with remaining string)
	* Both single digit and double digit, when the double digits are less than or equal to 26 (and call dfs again with remaining strings).

Our base case is when we have only a single digit left in our string or when we have nothing left in the string. In that case, we return 1 back up the recursion stack.

**Growing a tree**
![image](https://assets.leetcode.com/users/arkaung/image_1588418645.png)

**Dyanmic Programming**

We can see that this type of tree has a lot of **redundant sub-trees**. Dynamic Programming to the rescue!! (In my code, I use `lru_cache` decorator which essentially memoizes the function calls with argument-returned value pairs. So, when I call the same function with same arguements, and if that recursive call has been made before, it is just retrieved from memoized pair).

![image](https://assets.leetcode.com/users/arkaung/image_1588418649.png)

![image](https://assets.leetcode.com/users/arkaung/image_1588418654.png)

* After you have got a hang of the thinking process, we will have to handle issues with zeros.
	* Zeros can be in the middle or at the start.
		* If it is at the start, there is no way to decode the string.
		* If it is in the middle:
			* If it can be paired with the digit before zero (and is less than or equal to 26, then we can keep on growing our subtrees)
			* If it cannot be paired with the digit before zero, we have to destory that subtree together. This might even render the whole string undecodable. 


``` python
class Solution:
    def numDecodings(self, s:str) -> int:
        if len(s) == 0 or s is None:
            return 0

        @lru_cache(maxsize=None)
        def dfs(string):
            if len(string)>0:
                if string[0] == '0':
                    return 0
            if string == "" or len(string) == 1:
                return 1
            if int(string[0:2]) <= 26:
                first = dfs(string[1:])
                second = dfs(string[2:])
                return first+second
            else:
                return dfs(string[1:])

        result_sum = dfs(s)

        return result_sum
```