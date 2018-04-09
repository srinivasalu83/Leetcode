class Sol806 {
    public int[] numberOfLines(int[] widths, String S) {
        char[] chs = S.toCharArray();
        int numFullLines = 0;
        int lenCurrentLine = 0;
        for (char ch : chs) {
            int chLen = widths[ch - 'a'];
            if (chLen <= 100 - lenCurrentLine) {
                lenCurrentLine += chLen;
            }
            else {
                numFullLines += 1;
                lenCurrentLine = chLen;
            }
        }
        numFullLines += (lenCurrentLine != 0) ? 1 : 0;
        return new int[]{numFullLines, lenCurrentLine};
    }
}