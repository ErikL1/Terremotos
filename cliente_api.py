import requests

def get_earthquakes(min_magnitude=4.0, start_time="2024-01-01", end_time="2024-12-31"):

    url = "https://earthquake.usgs.gov/fdsnws/event/1/query"
    params = {
        "format": "geojson", 
        "starttime": start_time,
        "endtime": end_time,
        "minmagnitude": min_magnitude,
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status() 
        data = response.json()

        # Procesa los datos y devuelve la información relevante
        earthquakes = data.get("features", [])
        result = [
            {
                "place": eq["properties"]["place"],
                "magnitude": eq["properties"]["mag"],
                "time": eq["properties"]["time"],
            }
            for eq in earthquakes
        ]

        return result
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API: {e}")
        return []

# Uso del cliente
if __name__ == "__main__":
    earthquakes = get_earthquakes(min_magnitude=5.0)
    print("Terremotos recientes:")
    for eq in earthquakes[:10]:  # Mostrar los 10 primeros resultados
        print(f"Lugar: {eq['place']}, Magnitud: {eq['magnitude']}, Tiempo: {eq['time']}")
