def courseSchedule(numCourse, prerequisites):

    graph = {}
    inPos = [0] * numCourse

    for i in prerequisites:

        if i[1] not in graph:
            graph[i[1]] = [i[0]]
        else:
            graph[i[1]].append(i[0])

    for key in graph:
        print 'graph', key, graph[key]

    queue = []

    for i in xrange(numCourse):
        if i not in graph:
            queue.append(i)

    print queue
    # BFS
    N = len(queue)
    while N > 0:

        t = queue.pop(0)
        N -= 1
        print 'inner', t, queue 
        if t in graph:
            for i in graph[t]:
                graph[i].remove(t)

                if len(graph[i]) == 0:
                    queue.append(i)
                    N += 1

    for i in xrange(numCourse):
        try:
            if len(graph[i]) != 0:
                return False
        except:
            pass

    return True



print courseSchedule(2, [[1,0],])
