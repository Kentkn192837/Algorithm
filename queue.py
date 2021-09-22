def enqueue(queue, value):
    queue.append(value)
    return queue    

def dequeue(queue):
    if len(queue) == 0:
        return queue, None
    elm = queue.pop(0)
    return queue, elm

if __name__ == '__main__':
    n = [int(x) for x in input().rstrip().split(' ')]
    print(n)

    n = enqueue(n, 10)
    print(n)

    n, val = dequeue(n)
    print(n)
    print(val)

    a = []
    n, val = dequeue(a)
    print(n)
    print(val)
