import re
import random




matcher2 = re.compile(r'(\d+) (\d+)')
fmatcher2 = re.compile(r'(\d+\.\d+) (\d+\.\d+)')
matcher5 = re.compile(r'(\d+) (\d+) (\d+) (\d+) (\d+)')

def get_plan(filename):
    coords = []
    es = []
    with open(filename, 'r') as f:
        line = f.readline()
        (v_nb, e_nb, t_total, car_nb, start) = matcher5.search(line).groups()
        v_nb = int(v_nb)
        e_nb = int(e_nb)
        t_total = int(t_total)
        car_nb = int(car_nb)
        start = int(start)
        for i in xrange(v_nb):
            line = f.readline()
            g = fmatcher2.search(line).groups()
            coords.append(( float(g[0]) , float(g[1])   ))
        for j in xrange(e_nb):
            line = f.readline()
            g = matcher5.search(line).groups()

            es.append((int(g[0]), int(g[1]), int(g[2]), int(g[3]), int(g[4])   ))
    return (v_nb, e_nb, t_total, car_nb, start, coords, es)



def dumps(filename, solution):
    with open(filename, 'w') as f:
        f.write('{}\n'.format(len(solution)))
        for path in solution:
            f.write('{}\n'.format(len(path)))
            for v in path:
                f.write('{}\n'.format(v))


def convert_es(es):
    di = {}
    for e in es:
        (begin, end, direction, t, length) = e
        if begin not in di:
            di[begin] = []
        di[begin].append((end, t, length))
        if direction == 2:
            if end not in di:
                di[end] = []
            di[end].append((begin, t, length))

    return di



def ran_path(es_conv, start, t):
    time = 0
    res = [start]
    current_e = start
    while True:
        road = random.choice(es_conv[current_e])
        time += road[1]
        if time > t:
            break
        current_e = road[0]
        res.append(current_e)
    return res

def ran_solve(plan):
    es_conv = convert_es(plan[6])
    return [ran_path(es_conv, plan[4], plan[2]) for i in xrange(plan[3])]



def score(solution, es_conv):
    visited = set()
    score = 0
    for path in solution:
        current = path[0]
        for v in path[1:]:
            road = (min(v, current), max(v, current))
            if road not in visited:
                visited.add(road)
                try:
                    score += [ x for x in es_conv[current] if x[0] == v ][0][2]
                except:
                 print current, v, es_conv[current]
                 raise
                current = v
    return score

