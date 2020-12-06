time_of_start = input().split(":")
time_of_last_copy = 0
if int(time_of_start[1]) > 30 or (int(time_of_start[1]) == 30 and int(time_of_start[2]) > 0):
    time_of_last_copy = ":".join([time_of_start[0], "30", "00"])
elif int(time_of_start[1]) < 30 and int(time_of_start[1]) != 0:
    time_of_last_copy = ":".join([time_of_start[0], "00", "00"])
elif int(time_of_start[1]) == 00 and int(time_of_start[0]) == 00:
    time_of_start[0] = int(time_of_start[0]) - 1
    if time_of_start[0] < 0:
        time_of_start[0] = time_of_start[0] + 24
    time_of_start[0] = str(time_of_start[0])
    time_of_last_copy = ":".join([time_of_start[0], "30", "00"])
print(time_of_last_copy)
