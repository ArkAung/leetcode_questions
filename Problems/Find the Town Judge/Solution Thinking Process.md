[Answer on LeetCode](https://leetcode.com/problems/find-the-town-judge/discuss/625895/Python-Single-placeholder-array-O(n)-Runtime)

**Note**
* A Judge is one of the villagers too.

Visually speaking, we want to find the judge in this manner:

![image](https://assets.leetcode.com/users/arkaung/image_1589173490.png)

The way we are going to capture that incoming arrows count is by recoding the number of occurrence a villager shows up in the second
number in the `Trust` pair (since that villager is being trusted by some other villager and he/she might as well be the judge).

**But** the important thing to notice here is, if a villager is truly a judge, he/she must be trusted by `N-1` villagers (excluding him/herself).
* The second graph in the above image: see that 1 and 3 are not judges even though they are trusted by some other villagers but not by `N-1` villagers.

The way we are going to implement is by having a placeholder villager array which will keep track of:
* The trusted count of each villager

The trusted count will be added by 1 if the villager shows up as the second number while going though the `Trust` pairs.
The trusted count will be deducted by 1 if the villager shows up as the first number.

After we have finished going through the `Trust` list, we can go through villagers placeholder to look for an index which corresponds to `N-1` and this is our judge.