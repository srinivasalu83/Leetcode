/*
 * [804] Rotated Digits
 *
 * https://leetcode.com/problems/rotated-digits/description/
 *
 * algorithms
 * Easy (50.56%)
 * Total Accepted:    6.9K
 * Total Submissions: 13.6K
 * Testcase Example:  '10'
 *
 * X is a good number if after rotating each digit individually by 180 degrees,
 * we get a valid number that is different from X.  Each digit must be rotated
 * - we cannot choose to leave it alone.
 * 
 * A number is valid if each digit remains a digit after rotation. 0, 1, and 8
 * rotate to themselves; 2 and 5 rotate to each other; 6 and 9 rotate to each
 * other, and the rest of the numbers do not rotate to any other number and
 * become invalid.
 * 
 * Now given a positive number N, how many numbers X from 1 to N are good?
 * 
 * 
 * Example:
 * Input: 10
 * Output: 4
 * Explanation: 
 * There are four good numbers in the range [1, 10] : 2, 5, 6, 9.
 * Note that 1 and 10 are not good numbers, since they remain unchanged after
 * rotating.
 * 
 * 
 * Note:
 * 
 * 
 * N  will be in range [1, 10000].
 * 
 * 
 */
class Solution {
    public int rotatedDigits(int N) {
        int count = 0;
        for (int i = 1; i <= N; i++) {
            if (isValidDigit(i))
                count++;
        }
        return count;
    }
    
    private boolean isValidDigit(int N) {
        boolean isValid = false;
        while (N > 0) {
            int lastDigit = N % 10;
            if (lastDigit == 2 || lastDigit == 5 || lastDigit == 6 || lastDigit == 9)
                isValid = true;
            else if (lastDigit == 3 || lastDigit == 4 || lastDigit == 7)
                return false;
            N /= 10;
        }
        return isValid;
    }
}
