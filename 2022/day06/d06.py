
with open('06_example.txt', 'r') as input:
    data_buffer = input.read()

PACKET_MARKER_SIZE = 4
MESSAGE_MARKER_SIZE = 14


def find_marker(buffer, length):
    signal = []
    i = 0
    while(len(signal) != length and i < len(buffer)):
        if(buffer[i] in signal):
            signal.pop(0)
        else:
            signal.append(buffer[i])
            i += 1
    return i


print("Part 1 answer: ", find_marker(data_buffer, PACKET_MARKER_SIZE))
print("Part 2 answer: ", find_marker(data_buffer, MESSAGE_MARKER_SIZE))
