from collections import deque

datastream_file = open('./input.txt', 'r')
datastreams = datastream_file.readlines()
datastream_file.close()

datastream_buffer = deque(maxlen=14)

start_marker = 0
for char in datastreams[0]:
    start_marker += 1
    datastream_buffer.append(char)
    if len(datastream_buffer) >= 14:
        if len(datastream_buffer) == len(set(datastream_buffer)):
            print(datastream_buffer)
            print(start_marker)
            break
