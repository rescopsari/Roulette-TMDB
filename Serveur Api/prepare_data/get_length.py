def get_length(data):
    average = 0
    for duration in data:
        average += duration
    average /= len(data)
    return average