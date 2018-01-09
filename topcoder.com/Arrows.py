import re


class Arrows:
    
    def longestArrow(self, s):
        l_s = r"<-*"
        l_d = r"<=*"
        r_s = r"-*>"
        r_d = r"=*>"

        pattens = [l_s, l_d, r_s, r_d]

        max_len = -1

        for p in pattens:
            if re.findall(p, s):
                l = len(max(re.findall(p, s)))
                if l > max_len:
                    max_len = l

        return max_len
