n = int(input())

max_seq = 0
cur_seq = 1
last = -1

while n > 1:
    cur = int(input())

    if last == -1:
        last = cur
        continue

    if cur > last:
        cur_seq += 1
    else:
        if cur_seq > max_seq:
            max_seq = cur_seq
        cur_seq = 1

    last = cur
    n -= 1

if cur_seq > max_seq:
    max_seq = cur_seq

print(max_seq)
