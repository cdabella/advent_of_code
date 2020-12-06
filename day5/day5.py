# Seat identification (pt2) can be solved by either by using a dict or set to
# identify all seats present and looping through the entire 0b1111111111 == 1023
# set of seats or a list of seats present and sorting the list O(nlogn). If the
# plane is a Cessna, definitely want a sorted list

with open ('input.txt') as f:
    seats = set()
    max = 0
    while (line := f.readline()):
        seat = 0b0
        for character in line[:-1]:
            seat += 0b0 if character in 'FL' else 0b1
            seat = seat << 1
        seat = seat >> 1  ## Least significant bit shouldn't be shifted on final loop
        seats.add(seat)
        max = seat if seat > max else max
    print(f'The max seat is: {max}')

    for seat in range(1, 1023):
        if all([seat-1 in seats, seat not in seats, seat+1 in seats]):
            print(f'My seat is: {seat}')
