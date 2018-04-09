class Sol784 {
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