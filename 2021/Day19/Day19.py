import sys

ll = [x for x in open("input.txt").read().strip().split('\n\n')]

ll = [[eval("[" + x + "]") for x in l.split("\n")[1:]] for l in ll]

coord_remaps = [(0, 1, 2), (0, 2, 1), (1, 0, 2), (1, 2, 0), (2, 0, 1), (2, 1, 0)]
coord_negations = [(1, 1, 1), (1, 1, -1), (1, -1, 1), (1, -1, -1), (-1, 1, 1), (-1, 1, -1), (-1, -1, 1), (-1, -1, -1)]


def apply(remap, negat, scan):
    ret = []
    for item in scan:
        ret.append([negat[0] * item[remap[0]], negat[1] * item[remap[1]], negat[2] * item[remap[2]]])
    return ret


distances_from_scan_0 = [(0, 0, 0)]


def find_alignment(scan_a, scan_b):
    in_a = set([tuple(x) for x in scan_a])
    for remap in coord_remaps:
        for negat in coord_negations:
            a = scan_a
            b = apply(remap, negat, scan_b)
            for a_pos in a:
                for b_pos in b:
                    remap_by = [b_pos[0] - a_pos[0], b_pos[1] - a_pos[1], b_pos[2] - a_pos[2]]
                    matches = 0
                    all_remapped = []
                    for other_b in b:
                        remapped_to_a = (other_b[0] - remap_by[0], other_b[1] - remap_by[1], other_b[2] - remap_by[2])
                        if remapped_to_a in in_a:
                            matches += 1
                        all_remapped.append(list(remapped_to_a))
                    if matches >= 12:
                        print("match", remap_by)
                        distances_from_scan_0.append(tuple(remap_by))
                        return (True, all_remapped)
    return (False, None)


good = ll[0]
aligned_indices = set()
aligned_indices.add(0)
aligned = {}
aligned[0] = ll[0]
all_aligned = []
all_aligned += [tuple(x) for x in ll[0]]
noalign = set()
while len(aligned_indices) < len(ll):
    for i in range(len(ll)):
        if i in aligned_indices:
            continue
        for j in aligned_indices:
            print("Checking", i, "against", j)
            if (i, j) in noalign:
                continue
            ok, remap = find_alignment(aligned[j], ll[i])
            if ok:
                aligned_indices.add(i)
                aligned[i] = remap
                all_aligned += [tuple(x) for x in remap]
                break
            noalign.add((i, j))
print(len(set(all_aligned)))

dists = []
for a in distances_from_scan_0:
    for b in distances_from_scan_0:
        dists.append(sum([abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2])]))
print(max(dists))
