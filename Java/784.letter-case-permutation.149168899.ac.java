/*
 * [800] Letter Case Permutation
 *
 * https://leetcode.com/problems/letter-case-permutation/description/
 *
 * algorithms
 * Easy (52.49%)
 * Total Accepted:    9.1K
 * Total Submissions: 17.4K
 * Testcase Example:  '"a1b2"'
 *
 * Given a string S, we can transform every letter individually to be lowercase
 * or uppercase to create another string.  Return a list of all possible
 * strings we could create.
 * 
 * 
 * Examples:
 * Input: S = "a1b2"
 * Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
 * 
 * Input: S = "3z4"
 * Output: ["3z4", "3Z4"]
 * 
 * Input: S = "12345"
 * Output: ["12345"]
 * 
 * 
 * Note:
 * 
 * 
 * S will be a string with length at most 12.
 * S will consist only of letters or digits.
 * 
 */
class Solution {
    public List<String> letterCasePermutation(String S) {
        List<String> res = new LinkedList<String>();
        if (S == null)
            return res;
        dfs(S, res, 0);
        return res;
    }
    
    private void dfs(String s, List<String> res, int pos) {
        if (pos == s.length()) {
            res.add(s);
            return;
        }
        if (s.charAt(pos) >= '0' && s.charAt(pos) <= '9') {
            dfs(s, res, pos + 1);
            return;
        }
        char[] chs = s.toCharArray();
        chs[pos] = Character.toLowerCase(chs[pos]);
        dfs(String.valueOf(chs), res, pos + 1);
        chs[pos] = Character.toUpperCase(chs[pos]);
        dfs(String.valueOf(chs), res, pos + 1);
    }
}

