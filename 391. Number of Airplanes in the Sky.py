# Definition of Interval.
# class Interval(object):
#     def __init__(self, tuple):
#         self.start = tuple[0]
#         self.end = tuple[1]
class Solution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        # write your code here
        points = []
        for interval in airplanes:
            points.append([interval[0], 1])
            points.append([interval[1], -1])
            # points.append([interval.start, 1])
            # points.append([interval.end, -1])
        count, ans = 0, 0
        for _, count_delta in sorted(points):
            count += count_delta
            ans = max(count, ans)
        return ans


class Point(object):
    def __init__(self, time, flag):
        self.time = time  # current time
        self.flag = flag  # departure or arrival 1 is departure 0 is arrival

    def __lt__(self, other):
        if self.time == other.time:
            return self.flag < other.flag
        else:
            return self.time < other.time


class MySolution:
    """
    @param airplanes: An interval array
    @return: Count of airplanes are in the sky.
    """

    def countOfAirplanes(self, airplanes):
        # write your code here
        points = []
        for interval in airplanes:
            a = Point(interval[0], 1)
            b = Point(interval[1], 0)
            points.append(a)
            points.append(b)
        points.sort()
        count = 0
        ans = 0
        for ele in points:
            print(ele.flag, ele.time)
        for p in points:
            if p.flag == 1:
                count += 1
            else:
                count -= 1
            ans = max(count, ans)
        return ans


if __name__ == '__main__':
    S = Solution().countOfAirplanes([(1, 10), (2, 3), (5, 8), (4, 7)])
    print(S)
