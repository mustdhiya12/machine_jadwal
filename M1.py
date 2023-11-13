import cv2
file = 'cat.jpeg'
# Baca gambar
gambar1 = cv2.imread(file)

# Menampilkan informasi gambar
info = cv2.imread(file, cv2.IMREAD_ANYDEPTH)
print(info)

# Menampilkan gambar
print(cv2.imshow('Gambar', gambar1))
cv2.waitKey(0)
cv2.destroyAllWindows()
