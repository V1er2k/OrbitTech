import math

def haversine(lat1, lon1, lat2, lon2):
    R = 6371000  # радиус Земли в метрах

    # преобразование градусов в радианы
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    lat2_rad = math.radians(lat2)
    lon2_rad = math.radians(lon2)

    # разница широт и долгот
    dlat = lat2_rad - lat1_rad
    dlon = lon2_rad - lon1_rad

    # Формула
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    
    # Расстояние между точками на поверхности Земли
    distance = R * c

    return distance

def calculate_new_coordinates(lat1, lon1, bearing, speed, time):
    R = 6371000  # радиус Земли в метрах
    distance = speed * time  # расстояние пройденное за время

    # преобразование градусов в радианы
    lat1_rad = math.radians(lat1)
    lon1_rad = math.radians(lon1)
    bearing_rad = math.radians(bearing)

    # Формула для вычисления новой широты и долготы
    lat2 = math.asin(math.sin(lat1_rad) * math.cos(distance/R) + math.cos(lat1_rad) * math.sin(distance/R) * math.cos(bearing_rad))
    lon2 = lon1_rad + math.atan2(math.sin(bearing_rad) * math.sin(distance/R) * math.cos(lat1_rad), math.cos(distance/R) - math.sin(lat1_rad) * math.sin(lat2))

    # преобразование радиан в градусы
    lat2 = math.degrees(lat2)
    lon2 = math.degrees(lon2)

    return lat2, lon2

# Пример использования
lat1 = 37.7749  # начальная широта в градусах
lon1 = -122.4194  # начальная долгота в градусах
bearing = 45  # направление движения в градусах (север = 0, восток = 90)
speed = 10  # скорость в м/с
time = 3600  # время в секундах (в данном случае 1 час)

# Вычисление новых координат
new_lat, new_lon = calculate_new_coordinates(lat1, lon1, bearing, speed, time)

print("Новые координаты:", new_lat, new_lon)
