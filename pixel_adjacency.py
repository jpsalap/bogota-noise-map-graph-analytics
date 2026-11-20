import cv2
import numpy as np
from collections import defaultdict

# Load color-quantized locality image
imagen = cv2.imread('aprox_BarriosUnidos.png')
alto, ancho, _ = imagen.shape

with open('datos_pixeles_BarriosUnidos.txt', 'w') as archivo:
	archivo.write("Color1\tColor2\tRepeticion\n")
	relaciones = defaultdict(int)

	# Scan interior pixels (x, y) and count orthogonal + diagonal neighbor pairs
	for y in range(alto - 1):
		for x in range(1, ancho - 1):
			pixel = tuple(imagen[y, x])

			# Exclude exterior white background pixels (255, 255, 255)
			if not np.array_equal(pixel, [255, 255, 255]):
				color = f'{pixel[0]} - {pixel[1]} - {pixel[2]}'

				# Right neighbor
				pixel_derecha = tuple(imagen[y, x + 1])
				if not np.array_equal(pixel_derecha, [255, 255, 255]):
					color_derecha = f'{pixel_derecha[0]} - {pixel_derecha[1]} - {pixel_derecha[2]}'
					relaciones[(color, color_derecha)] += 1

				# Bottom neighbor
				pixel_abajo = tuple(imagen[y + 1, x])
				if not np.array_equal(pixel_abajo, [255, 255, 255]):
					color_abajo = f'{pixel_abajo[0]} - {pixel_abajo[1]} - {pixel_abajo[2]}'
					relaciones[(color, color_abajo)] += 1

				# Bottom-right diagonal neighbor
				pixel_diag_der_abajo = tuple(imagen[y + 1, x + 1])
				if not np.array_equal(pixel_diag_der_abajo, [255, 255, 255]):
					color_diag_der_abajo = f'{pixel_diag_der_abajo[0]} - {pixel_diag_der_abajo[1]} - {pixel_diag_der_abajo[2]}'
					relaciones[(color, color_diag_der_abajo)] += 1

				# Bottom-left diagonal neighbor
				pixel_diag_izq_abajo = tuple(imagen[y + 1, x - 1])
				if not np.array_equal(pixel_diag_izq_abajo, [255, 255, 255]):
					color_diag_izq_abajo = f'{pixel_diag_izq_abajo[0]} - {pixel_diag_izq_abajo[1]} - {pixel_diag_izq_abajo[2]}'
					relaciones[(color, color_diag_izq_abajo)] += 1

	for combinacion, repeticion in relaciones.items():
		archivo.write(f'{combinacion[0]}\t{combinacion[1]}\t{repeticion}\n')

print("Adjacent color combinations saved to 'datos_pixeles_BarriosUnidos.txt'")