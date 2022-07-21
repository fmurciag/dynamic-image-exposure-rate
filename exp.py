import cv2
import numpy as np
import os
 
def gamma_trans (img, gamma): # procesamiento de la función gamma
         gamma_table = [np.power (x / 255.0, gamma) * 255.0 for x in range(256)] # Crear una tabla de mapeo
         gamma_table = np.round (np.array (gamma_table)).astype (np.uint8) #El valor del color es un número entero
         return cv2.LUT (img, gamma_table) #Tabla de búsqueda de color de imagen. Además, se puede diseñar un algoritmo adaptativo de acuerdo con el principio de homogeneización de la intensidad de la luz (color).
def nothing(x):
    pass

cv2.namedWindow ("demo", 0) #Adaptar el tamaño de la ventana de visualización a la resolución del monitor
cv2.createTrackbar ('Valor de Gamma', 'demo', 100,1000, nothing) # Use el control deslizante para ajustar dinámicamente el parámetro gamma

data_base_dir = "C:/Users/fmurc/Desktop/dynamic-image-exposure-rate/img_in/" # Ingrese la ruta de la carpeta
outfile_dir = "C:/Users/fmurc/Desktop/dynamic-image-exposure-rate/img_out/" # La ruta de la carpeta de salida
processed_number = 0 # Cuente el número de imágenes procesadas


print ("press enter to make sure your operation and process the next picture")

for file in os.listdir (data_base_dir): # atraviesa la imagen de la carpeta de destino
    read_img_name = data_base_dir + "/" + file # Obtiene la ruta completa de la imagen
    print(read_img_name)
    image = cv2.imread (read_img_name) # Lee la imagen
    while(1):
        value_of_gamma = cv2.getTrackbarPos ('Valor de Gamma', 'demo') # valor de gamma
        value_of_gamma = value_of_gamma * 0.01 # Comprime el rango de gamma para un ajuste fino
        image_gamma_correct = gamma_trans (image, value_of_gamma) # 2.5 es el valor exponencial de la función gamma, más de 1 disminución de exposición, mayor de 0 menos de 1 mejora de exposición
        cv2.imshow("demo",image_gamma_correct)
        k=cv2.waitKey(1)
        if k == 13: #Presione Enter para confirmar el procesamiento, guarde la imagen en la carpeta de salida y lea la siguiente imagen
            processed_number+=1
            out_img_name=outfile_dir+'//'+file.strip()
            cv2.imwrite(out_img_name,image_gamma_correct)
            print("The number of photos which were processed is "),processed_number
            break

    