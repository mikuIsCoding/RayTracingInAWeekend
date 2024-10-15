import numpy as np
from vec3 import Vec3
def writeImage(file_name: str, pixels):
    height = len(pixels)
    width = len(pixels[0])
    with open(file_name, "w") as f:
        f.write(f"P3 {width} {height} 255")
        for i in range(height):
            for j in range(width):
                f.write(f" {pixels[i][j][0]}")
                f.write(f" {pixels[i][j][1]}")
                f.write(f" {pixels[i][j][2]}")

def generated_pixels(width, height):
    result = []
    for i in range(height):
        row = []
        for j in range(width):
            r = float(i) / (width-1)
            g = float(j) / (height-1)
            b = 0

            ir = int(255.999 * r)
            ig = int(255.999 * g)
            ib = int(255.999 * b)
            row.append((ir, ig, ib))

        result.append(row)

    return result

# image = generated_pixels(800, 600)
# writeImage("image.ppm", image)
vec = Vec3(0.0, 0.0, 1.0)
vec2 = Vec3(2.0, 3.0, 2.0)
vec = vec / 2
print(vec)
