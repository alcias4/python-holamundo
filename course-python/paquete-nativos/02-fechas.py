# import time

# print(time.time())


from datetime import datetime

fecha = datetime(2023, 1, 1)
fecha_2 = datetime(2023, 2, 1)

ahora = datetime.now()

fecha_str = datetime.strptime("2023-01-03", "%Y-%m-%d")
print(ahora.strftime("%Y.%m.%d"))
print(fecha > fecha_2)


print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.minute
)
