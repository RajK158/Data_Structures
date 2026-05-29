# Problem: Minimum Window Substring
# Pattern: Sliding Window + HashMap
# Time: O(n)
# Space: O(m)

class Solution:

    def minWindow(self, s: str, t: str) -> str:

        if t == "":
            return ""

        count_t = {}
        window = {}

        for c in t:
            count_t[c] = 1 + count_t.get(c, 0)

        have = 0
        need = len(count_t)

        res = [-1, -1]
        res_len = float("inf")

        l = 0

        for r in range(len(s)):

            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in count_t and window[c] == count_t[c]:
                have += 1

            while have == need:

                if (r - l + 1) < res_len:
                    res = [l, r]
                    res_len = r - l + 1

                window[s[l]] -= 1

                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1

                l += 1

        l, r = res

        if res_len == float("inf"):
            return ""

        return s[l:r + 1]


if __name__ == "__main__":

    sol = Solution()

    print(sol.minWindow("OUZODYXAZV", "XYZ"))  # YXAZ
    print(sol.minWindow("xyz", "xyz"))         # xyz
    print(sol.minWindow("x", "xy"))            # ""