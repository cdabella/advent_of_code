from joblib import Parallel, delayed

with open ('input.txt') as f:
    arrival = int(f.readline().strip())
    buses = [x for x in f.readline().strip().split(',')]

def make_constraint(pos, bus_id):
    def constraint(t):
        return ((t + pos) % bus_id == 0)
    return constraint

constraints = []

for i, id in enumerate(buses):
    if id != 'x':
        constraints.append(make_constraint(i, int(id)))

def solver(times):
    for time in times:
        if all([constraint(time) for constraint in constraints]):
            # print(time)
            return time
    return 0

with Parallel(n_jobs=-4) as parallel:
    time = 0
    n_iter = 0
    while time == 0:
        results = parallel(delayed(solver)(times)
            for times in [range(start*1000, start*1000 + 1000)
                          for start in range(n_iter*10, n_iter*10 + 10)])
        results = [result for result in results if result != 0]
        if len(results) > 0:
            time = min(results)
        n_iter += 1

    print(time)
