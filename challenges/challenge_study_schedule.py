def study_schedule(permanence_period, target_time):
    if type(target_time) != int or target_time < 0:
        return None

    count = 0
    for start, end in permanence_period:
        if type(start) != int or type(end) != int or start > end:
            return None
        if start <= target_time <= end:
            count += 1
    return count
