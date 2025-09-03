class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9: #base case
            digits[-1] += 1
            return digits


        i = len(digits) - 1
        while digits[i] == 9 and i >= 0: # finds right-most index of not 9
            digits[i] = 0
            i -= 1

        if i < 0: # if all were nine
            return [1] + digits
        else:
            digits[i] += 1
        return digits


# 0 ms, beats 100%. and 95% my own work (i asked chat for a nudge in the right direction twice)

#summary:
# i did way too much at first. I got the base case easy, but tried checking for all nines first, then looping again if they were not.
# pattern: math and array, nothing crazy
# edge case: all nines, empty list, last element is not 9. Should add base case for empty list but eh too lazy now
# gotcha: just need practice with loops and iteration. got myself confused but I was always on the right track.
                




        