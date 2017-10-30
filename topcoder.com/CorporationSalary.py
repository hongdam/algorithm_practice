import functools


class CorporationSalary:
    #     def deco(func):
    #         cache = {}
    #
    #         def decorated_func(*args):
    #             if args in cache:
    #                 return cache[args]
    #             else:
    #                 cache[args] = func(*args)
    #                 return cache[args]
    #
    #         return decorated_func

    @functools.lru_cache()
    def _getSalary(self, i):

        salary = 0
        relation = self.relations[i]

        for j, r in enumerate(relation):
            if r == 'Y':
                salary += self._getSalary(j)

        if salary == 0:
            return 1
        else:
            return salary

    def totalSalary(self, relations):
        self.relations = relations

        total = 0

        for i in range(len(relations)):
            total += self._getSalary(i)

        return total


c = CorporationSalary()
r = ["NNYN", "NNYN", "NNNN", "NYYN"]
print(c.totalSalary(r))
