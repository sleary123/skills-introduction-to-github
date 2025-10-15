import sys

def count_right_triangles_integer_debug(points):
    n = len(points)
    total = 0

    for i in range(n):
        xA, yA = points[i]
        vectors = []

        for j in range(n):
            if i == j:
                continue
            xB, yB = points[j]
            dx, dy = xB - xA, yB - yA
            if dx == 0 and dy == 0:
                continue
            vectors.append((dx, dy))

        # no need to dedup yet
        m = len(vectors)
        for u in range(m):
            x1, y1 = vectors[u]
            for v in range(u + 1, m):
                x2, y2 = vectors[v]
                if x1 * x2 + y1 * y2 == 0:
                    total += 1
                    # Print info for debugging
                    print(f"Right angle at point {points[i]} using vectors {vectors[u]} and {vectors[v]}")

    return total

def read_points_from_file(filename):
    points = []
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines[1:]:
            x_str, y_str = line.strip().split()
            x, y = int(x_str), int(y_str)
            points.append((x, y))
    return points

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        filename = input("Enter the filename containing the points: ").strip()

    try:
        points = read_points_from_file(filename)
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        sys.exit(1)

    count = count_right_triangles_integer(points)
    print(f"The number of unique right triangles is: {count}")

