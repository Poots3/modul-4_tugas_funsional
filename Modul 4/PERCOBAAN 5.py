#percobaan 5
def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    def calculate_m(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    M = calculate_m(p1, p2)

    C = p1[1] - M * p1[0]

    return f"y = {M:.2f}x + {C:.2f}"


print("Persamaan garis yang melalui titik A dan B:")
print(line_equation_of(point(1, 3), point(7, 7)))

print("Persamaan garis untuk NIM akhir kalian:")
print(line_equation_of(point(7, 1), point(7, 3)))