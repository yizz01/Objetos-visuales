import folium

# Coordenadas del centro de El Salvador
lat = 13.794185
lon = -88.89653

# Crea el mapa y centra la vista en El Salvador
mapa = folium.Map(location=[lat, lon], zoom_start=8)

# Crea un diccionario con los nombres y coordenadas de los departamentos 
coords_departamentos = {
    'Ahuachapán': [13.9200784, -89.8454882],
    'Cabañas': [13.9159079, -88.9248535],
    'Chalatenango': [14.0771045, -88.9553363],
    'Cuscatlán': [13.8139705, -88.8502381],
    'La Libertad': [13.6782252, -89.2788627],
    'La Paz': [13.5414203, -88.9898523],
    'La Unión': [13.3332334, -87.8493448],
    'Morazán': [13.7579084, -88.1271555],
    'San Miguel': [13.4506578, -88.1760676],
    'San Salvador': [13.6944523, -89.2872291],
    'Santa Ana': [13.9950085, -89.5597993],
    'San Vicente': [13.6455663, -88.8743807],
    'Sonsonate': [13.7193739, -89.729679],
    'Usulután': [13.3422911, -88.5116217]
}

# Dibuja un marcador para cada departamento
for departamento, coords in coords_departamentos.items():
    folium.Marker(location=coords, popup=departamento).add_to(mapa)

# Guarda el mapa en un archivo HTML
mapa.save("el_salvador_departamentos.html")
