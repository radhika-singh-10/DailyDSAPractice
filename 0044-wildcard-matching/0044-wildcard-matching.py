class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)

        # The base cases
        if p == s or set(p) == {"*"}:
            return True
        if p == "" or s == "":
            return False
        d = [[False] * (s_len + 1) for _ in range(p_len + 1)]
        d[0][0] = True
        for p_idx in range(1, p_len + 1):
            if p[p_idx - 1] == "*":
                s_idx = 1
                while not d[p_idx - 1][s_idx - 1] and s_idx < s_len + 1:
                    s_idx += 1
                d[p_idx][s_idx - 1] = d[p_idx - 1][s_idx - 1]
                while s_idx < s_len + 1:
                    d[p_idx][s_idx] = True
                    s_idx += 1
            elif p[p_idx - 1] == "?":
                for s_idx in range(1, s_len + 1):
                    d[p_idx][s_idx] = d[p_idx - 1][s_idx - 1]
            else:
                for s_idx in range(1, s_len + 1):
                    d[p_idx][s_idx] = (
                        d[p_idx - 1][s_idx - 1] and p[p_idx - 1] == s[s_idx - 1]
                    )

        return d[p_len][s_len]