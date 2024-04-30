import csv

# Datos proporcionados
data = [
    ["Real Madrid", 2.2, 12.6, 0.1, 6.2, 10.1, 1.5, 1.2, 14.5, 0.2, 52],
    ["Bayern Munich", 1.8, 10.4, 0.2, 5.5, 9.9, 1.8, 0.9, 9.6, 0.2, 57],
    ["Borussia Dortmund", 1.5, 10.1, 0.1, 5.7, 9.5, 1.7, 0.9, 14.3, 0.3, 48],
    ["Paris Saint-Germain", 1.9, 12.3, 0.3, 7.4, 10.9, 3, 1.3, 11.3, 0, 65]
]

# Cabeceras de las columnas
headers = ["equipo", "media_goles_ataque", "tiros_puerta", "penaltis_favor", "corners", "faltas_recibidas",
           "fuera_juego", "goles_recibidos", "tiros_puerta_recibidos", "penalti_contra", "posesion"]

# Escribir los datos en un archivo CSV
with open('semis/datos_semis.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # Escribir las cabeceras
    writer.writerow(headers)
    # Escribir los datos
    writer.writerows(data)
