# Centro-de-gravedad
Método segmentario para el cálculo del centro de gravedad de personas en imágenes jpg

El archivo DIGITALIZAR.py sirve para identificar las coordenadas de los 21 puntos del método segmentario sobre imágenes JPG, las coordenadas se guardan en un archivo de tipo TXT nombrado c_real.txt; las imágenes deben estar en la misma carpata que este archivo. 
Las coordenadas del archivo c_real.txt son coordandas del mundo real, transformadas de las coordenadas digitalizadas oprimiendo el notón izquierdo del ratón (no hay manera de corregir errores de captura, por lo que se sugiere borrar inicialmente el archivo donde se guardan dichas coordenadas).

El archivo mp4TOjpg.py transforma un video mp4 a imagenes jpg en la misma carpeta donde se encuentra este archivo. Funciona como herramienta de apoyo para la digitalización.



El archivo CG.py integra en primer versión todos los módulos anteriores y agrega:
#### * modelo de alambre
#### * calculo del centro de gravedad
