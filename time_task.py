from datetime import datetime, time

t3 = ['00:00:00', '00:01:11', '02:15:59', '23:59:58', '23:59:59']

def time_to_seconds(time_str):
    hours, minutes, seconds = map(int, time_str.split(':'))
    return hours * 3600 + minutes * 60 + seconds

def minimumDays(log):
    if not log:
        return 0

    count_days = 1
    time_seconds = [time_to_seconds(time_str) for time_str in log]
    last_time = time_seconds[0]

    for t in time_seconds[1:]:
        current_time = t

        if last_time > current_time:
            count_days += 1

        if last_time == current_time:
            count_days += 1

        last_time = current_time

    return count_days

# Тестовые случаи
print(minimumDays(t3))  # Должно выводиться: 1







