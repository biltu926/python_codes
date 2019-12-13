class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s

        T = [[0 for i in range(n)] for y in range(n)]
        max_length = 0
        default = s[0]
        max_string = ''

        for i in range(n):
            T[i][i] = True

        k = 2
        while k <= n:
            i = 0
            while i < n - k + 1:
                j = i + k - 1
                if s[i] == s[j] and T[i + 1][j] and k <= 2:
                    T[i][j] = True
                    if k > max_length:
                        max_length = k
                        max_string = s[i:j + 1]

                if s[i] == s[j] and T[i + 1][j - 1]:
                    T[i][j] = True
                    if k > max_length:
                        max_length = k
                        max_string = s[i:j + 1]
                i = i + 1
            k = k + 1
        if max_string == '':
            max_string = default
        return max_string

def main():
    s = Solution()
    print(s.longestPalindrome('bab'))


if __name__=='__main__':
    main()
