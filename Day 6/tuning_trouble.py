file = open('tuning_trouble').read().splitlines()
text = list(file[0])


def check_for_marker(items, size_limit) -> bool:
    return len(set(items)) == size_limit


def get_marker_char_count(size_limit) -> int:
    datastream_queue_buffer, count = [], 0

    for e in text:
        datastream_queue_buffer.append(e)
        count += 1

        if len(datastream_queue_buffer) == size_limit:
            if check_for_marker(datastream_queue_buffer, size_limit):
                break
            datastream_queue_buffer.pop(0)

    return count


print(get_marker_char_count(4), 'characters needed to be processed until first marker.')
print(get_marker_char_count(14), 'characters needed to be processed until first message marker.')
