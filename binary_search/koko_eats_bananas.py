"""
Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.
Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 10

"""

import math

"""
Solution:
The intuition is that the number of hours is at least equal to the number of piles so if Koko's eating speed is the largest pile
then it will finish all the bananas under h hours but we want the minimum speed. We can use binary search:
Start with 1 as the left boundary and the right boundary can be the largest pile. 
Step 1: Find the middle and calculate the time spent with middle as the eating speed
Step 2: if time spent is <= h then right becomes middle (which means we can go lower), else left is middle + 1
Step 3: Repeat until the boundaries overlap at which point we can return either left or right
"""
def minEatingSpeed(piles, hours):

    left = 1
    right = max(piles)

    while left < right:
        mid = (left + right) // 2
        hours_spent = 0

        for pile in piles:
            hours_spent += math.ceil(pile / mid)

        if hours_spent <= hours:
            right = mid
        else:
            left = mid + 1
    
    return right

def main():
    input = [30,11,23,4,20]

    print(f'min eating speed: {minEatingSpeed(input, 6)}')

if __name__ == "__main__":
    main()

