with open ('input.txt') as f:
    arrival = int(f.readline().strip())
    raw_buses = [x for x in f.readline().strip().split(',')]

N = 1
buses = []
for i, bus_id in enumerate(raw_buses):
    if bus_id == 'x':
        continue
    N *= int(bus_id)
    # (remainder, base)
    buses.append((int(bus_id) - i, int(bus_id)))

answer = 0

# Use direct construction of the chinese remainder theorem
# Sieve method would likely perform better
for (remainder, base) in buses:
    y = N // base
    y_inv = pow(y, -1, base)

    answer += remainder*y*y_inv

print(answer % N)
