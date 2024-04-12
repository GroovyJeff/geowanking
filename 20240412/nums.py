import numpy as np

# from https://codereview.stackexchange.com/questions/250855/efficiently-find-all-the-pythagorean-triplets-where-all-numbers-less-than-1000/250916#250916 (edited to provide only primitive triplets)

def triplets(N):
    mns = [(2, 1)]
    for m, n in mns:
        c = m*m + n*n
        if c <= N:
            a = m*m - n*n
            b = 2 * m * n
            for k in range(1,2):
                yield k*a, k*b, k*c
            mns += (2*m-n, m), (2*m+n, m), (m+2*n, n)


n = 10000000

trips = np.array(list(triplets(n)))

trans = np.transpose(trips)

both = np.intersect1d(trans[0], trans[1])

mask1 = np.isin(trips[:, 0], both)

print(trips[mask1])
