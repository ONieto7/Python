import cv2
import face_recognition as fr
import face_recognition
print("Face Recognition y sus dependencias están instaladas correctamente.")

# Cargar Imagens
foto_control = fr.load_image_file("FotoA.JPG")
foto_prueba = fr.load_image_file("FotoC.jpg")

# Pasar imagen a rgb
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

# Localizar cara control
face_cara_A = fr.face_locations(foto_control)[0]
cara_codifiacada_A = fr.face_encodings(foto_control)[0]

# Localizar cara control
face_cara_B = fr.face_locations(foto_control)[0]
cara_codifiacada_B = fr.face_encodings(foto_control)[0]

# Mostrar rectangulos
cv2.rectangle(foto_control, 
              (face_cara_A[3], face_cara_A[0]), 
              (face_cara_A[1], face_cara_A[2]), 
              (0, 255, 0), 
              2)

cv2.rectangle(foto_prueba,
                (face_cara_B[3], face_cara_B[0]), 
                (face_cara_B[1], face_cara_B[2]), 
                (0, 255, 0), 
                2)

# Realizar comparacion
resultado = fr.compare_faces([cara_codifiacada_A], cara_codifiacada_B)

print("Resultado: ", resultado)

# Mostrar imagenes
cv2.imshow("Foto Control", foto_control)
cv2.imshow("Foto Prueba", foto_prueba)

# medida de la distancia
distancia = fr.face_distance([cara_codifiacada_A], cara_codifiacada_B)