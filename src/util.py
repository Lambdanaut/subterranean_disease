def add_vectors(t1, t2):
    return tuple(map(lambda vec: vec[0] + vec[1], zip(t1, t2)))
