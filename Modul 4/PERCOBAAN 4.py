#PERCOBAAN 4

def translasi(tx, ty):
    def transformasi(p):
        x, y = p
        return x + tx, y + ty
    return transformasi

def dilatasi(sx, sy):
    def transformasi(p):
        x, y = p
        return x * sx, y * sy
    return transformasi

def rotasi(sudut):
    import math
    def transformasi(p):
        x, y = p
        x_baru = x * math.cos(math.radians(sudut)) - y * math.sin(math.radians(sudut))
        y_baru = x * math.sin(math.radians(sudut)) + y * math.cos(math.radians(sudut))
        return x_baru, y_baru
    return transformasi

titik = (3, 5)

translasi_2_minus_1 = translasi(2, -1)
dilatasi_2_minus_1 = dilatasi(2, -1)
rotasi_30_degrees = rotasi(30)

titik_setelah_translasi = translasi_2_minus_1(titik)
titik_setelah_dilatasi = dilatasi_2_minus_1(titik)
titik_setelah_rotasi = rotasi_30_degrees(titik)

print("Koordinat setelah translasi:", titik_setelah_translasi)
print("Koordinat setelah dilatasi:", titik_setelah_dilatasi)
print("Koordinat setelah rotasi:", titik_setelah_rotasi)