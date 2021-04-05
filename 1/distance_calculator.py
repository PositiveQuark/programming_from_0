# I


# Constants
SECONDS_PER_HOUR = 60 * 60
METERS_PER_KM = 1000

speed_m_per_second = 18
time_hours = 3
speed_km_per_hour = speed_m_per_second * SECONDS_PER_HOUR /  METERS_PER_KM
distance_km = speed_km_per_hour * time_hours
print(distance_km)