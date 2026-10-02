from typing import List


class Solution:

    def mergeTriplets(
        self,
        triplets: List[List[int]],
        target: List[int]
    ) -> bool:

        good = set()

        for triplet in triplets:

            if (
                triplet[0] > target[0]
                or triplet[1] > target[1]
                or triplet[2] > target[2]
            ):
                continue

            for i in range(3):

                if triplet[i] == target[i]:
                    good.add(i)

        return len(good) == 3


if __name__ == "__main__":

    sol = Solution()

    print(sol.mergeTriplets(
        [[1,2,3], [7,1,1]],
        [7,2,3]
    ))  # True

    print(sol.mergeTriplets(
        [[2,5,6], [1,4,4], [5,7,5]],
        [5,4,6]
    ))  # False