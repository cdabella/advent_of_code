with open ('input.txt') as f:
    arrival = int(f.readline().strip())
    buses = [int(x) for x in f.readline().strip().split(',') if x != 'x']

time = arrival
bus_id = False
while not bus_id:
    time += 1
    for bus in buses:
        if time % bus == 0:
            bus_id = bus
            break

print(time, bus_id)
print(bus_id * (time - arrival))
