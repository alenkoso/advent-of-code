from collections import deque
from itertools import permutations, combinations
import numpy as np

def parse_input(filename="input.txt"):
    scanners = []
    current_scanner = []
    
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith("---"):
                if current_scanner:
                    scanners.append(current_scanner)
                current_scanner = []
            else:
                x, y, z = map(int, line.split(","))
                current_scanner.append((x, y, z))
    if current_scanner:
        scanners.append(current_scanner)
    return scanners

def get_scanner_fingerprints(scanner):
    # Get a unique fingerprint for a scanner based on distances between points
    fingerprint = set()
    for i, p1 in enumerate(scanner):
        for p2 in scanner[i+1:]:
            dx = p1[0] - p2[0]
            dy = p1[1] - p2[1]
            dz = p1[2] - p2[2]
            d = dx*dx + dy*dy + dz*dz
            fingerprint.add(d)
    return fingerprint

def find_matching_pairs(scanners):
    # Find pairs of scanners that might overlap
    n = len(scanners)
    fingerprints = [get_scanner_fingerprints(s) for s in scanners]
    pairs = []
    
    for i in range(n):
        for j in range(i+1, n):
            if len(fingerprints[i] & fingerprints[j]) >= 66:  # 12 points make 66 distances
                pairs.append((i, j))
    
    return pairs

def align_scanner(base_points, scanner):
    # Try to align scanner with base_points
    base_set = set(base_points)
    
    # Try all possible rotations
    for px, py, pz in permutations([0, 1, 2]):
        for sx, sy, sz in [(1,1,1), (1,1,-1), (1,-1,1), (1,-1,-1),
                          (-1,1,1), (-1,1,-1), (-1,-1,1), (-1,-1,-1)]:
            # Create rotation function
            def rotate(p):
                x = p[px] * sx
                y = p[py] * sy
                z = p[pz] * sz
                return (x, y, z)
            
            rotated = [rotate(p) for p in scanner]
            
            # Try different reference points
            for i, bp in enumerate(base_points):
                for j, rp in enumerate(rotated):
                    # Calculate offset
                    offset = (bp[0] - rp[0], bp[1] - rp[1], bp[2] - rp[2])
                    
                    # Apply offset to all points
                    transformed = set()
                    for p in rotated:
                        transformed.add((p[0] + offset[0], 
                                      p[1] + offset[1], 
                                      p[2] + offset[2]))
                    
                    # Check for matches
                    matches = len(transformed & base_set)
                    if matches >= 12:
                        return list(transformed), offset
            
    return None, None

def solve_part1(scanners):
    pairs = find_matching_pairs(scanners)
    n = len(scanners)
    
    # Start with scanner
    aligned = {0}
    all_beacons = set(scanners[0])
    scanner_positions = [(0,0,0)]
    
    # Process pairs until all scanners are aligned
    while len(aligned) < n:
        for i, j in pairs:
            if i in aligned and j not in aligned:
                transformed, pos = align_scanner(list(all_beacons), scanners[j])
                if transformed:
                    all_beacons.update(transformed)
                    aligned.add(j)
                    scanner_positions.append(pos)
            elif j in aligned and i not in aligned:
                transformed, pos = align_scanner(list(all_beacons), scanners[i])
                if transformed:
                    all_beacons.update(transformed)
                    aligned.add(i)
                    scanner_positions.append(pos)
    
    return len(all_beacons), scanner_positions


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

def solve_part2(scanner_positions):
    max_dist = 0
    for i, pos1 in enumerate(scanner_positions):
        for pos2 in scanner_positions[i+1:]:
            dist = manhattan_distance(pos1, pos2)
            max_dist = max(max_dist, dist)
    return max_dist



def main():
    scanners = parse_input()
    result, scanner_positions = solve_part1(scanners)
    print(f"Part 1: {result}")
    print(f"Part 2: {solve_part2(scanner_positions)}")

if __name__ == "__main__":
    main()