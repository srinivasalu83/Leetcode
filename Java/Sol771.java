class Sol771 {
    public int numJewelsInStones(String J, String S) {
        char[] stones = S.toCharArray();
        int count = 0;
        for (int i = 0; i < stones.length; i++) {
            if (J.indexOf(stones[i]) != -1)
                count++;
        }
        return count;
    }
}