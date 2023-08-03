import time

size = int(input("Укажите размер файла для скачивания: "))
speed = int(input("Укажите скорость скачивания файла? "))
time_counter = 1
for mb in range(speed, size, speed):
    print(f"Прошло {time_counter} сек. Скачано {mb} из {size} Мб ({round(100 * mb / size)}%)")
    time_counter += 1
    time.sleep(1)
else:
    print(f"Прошло {time_counter} сек. Скачано {size} из {size} Мб ({round(100 * size / size)}%)")
