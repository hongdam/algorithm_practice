class Bonuses:
    def getDivision(self, points):
        total_p = sum(points)

        div_result = [int(x / total_p * 100) for x in points]

        remain_p = 100 - sum(div_result)

        idxs_plus = []
        sorted_p = sorted(set(points), reverse=True)

        for p in sorted_p:
            if remain_p <= 0:
                break
            idxs = [i for i, x in enumerate(points) if x == p]
            if len(idxs) <= remain_p:
                idxs_plus += idxs
                # idxs_plus.append(idxs)
                remain_p -= len(idxs)
            else:
                idxs_plus += idxs[:remain_p]
                # idxs_plus.append(idxs[:remain_p])
                remain_p = 0

        for i in idxs_plus:
            div_result[i] += 1

        return div_result

#    def indices_of(self, li, val):
#        return [i for i, x in enumerate(li) if x == val]