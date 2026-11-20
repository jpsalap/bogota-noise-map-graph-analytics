import numpy as np
import cv2
import matplotlib.pyplot as plt

# Load locality noise map image
image = cv2.imread('AntonioNarino.png')

# Define canonical target colors from Resolution 0627 of 2006 (in BGR format for OpenCV)
target_colors = np.array([
	[180, 224, 198],  # Light green | <= 35 dB
	[20, 142, 86],    # Green       | 35.1 - 40 dB
	[51, 102, 0],     # Dark green  | 40.1 - 45 dB
	[0, 255, 255],    # Yellow      | 45.1 - 50 dB
	[0, 204, 255],    # Ochre       | 50.1 - 55 dB
	[0, 138, 255],    # Orange      | 55.1 - 60 dB
	[52, 66, 227],    # Cinnabar    | 60.1 - 65 dB
	[28, 51, 204],    # Carmine     | 65.1 - 70 dB
	[138, 76, 222],   # Lilac red   | 70.1 - 75 dB
	[255, 0, 0],      # Blue        | 75.1 - 80 dB
	[128, 0, 0],      # Dark blue   | > 80 dB
	[255, 255, 255],  # White       | Exterior background
])

# Reshape target colors to broadcast against image dimensions (H, W, 1, 3)
target_colors = target_colors.reshape(1, -1, 3)

# Compute 3D Euclidean distance between every pixel and each reference color
distances = np.sqrt(np.sum((image[:, :, np.newaxis, :] - target_colors) ** 2, axis=3))

# Assign each pixel to its nearest canonical color
nearest_indices = np.argmin(distances, axis=2)
approximated_image = target_colors[0, nearest_indices]

# Convert BGR to RGB for Matplotlib visualization
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
approximated_image_rgb = cv2.cvtColor(approximated_image.astype(np.uint8), cv2.COLOR_BGR2RGB)

plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(image_rgb)
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(approximated_image_rgb)
plt.title('Approximated Image')
plt.axis('off')
plt.show()

# Save quantized image in lossless PNG format
cv2.imwrite('aprox_img.png', approximated_image)