from bisect import *
def add_interval(intervals, left, right):
    if left == right:
        return len(intervals)
    index = intervals.bisect_left((left, right))
    end_index = index
    while end_index < len(intervals) and intervals[end_index][0] <= right:
        right = max(right, intervals[end_index][1])
        end_index += 1
    del intervals[index:end_index]
    if index > 0 and intervals[index - 1][1] >= left:
        index -= 1
        left = min(left, intervals[index][0])
        right = max(right, intervals[index][1])
        del intervals[index]
    intervals.add((left, right))
    return intervals.bisect_left((left, right))

def remove_interval(intervals, left, right):
    if left == right:
        return
    index = add_interval(intervals, left, right)
    merged_left, merged_right = intervals[index]
    del intervals[index]
    if merged_left != left:
        intervals.add((merged_left, left))
    if right != merged_right:
        intervals.add((right, merged_right))