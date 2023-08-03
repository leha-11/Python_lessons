print("Укажите размер файла для скачивания:")
size = int(input())
print("Укажите скорость скачивания файла?")
speed = int(input())
download_size = 0
download_time = 1
while download_size <= size:
    download_time += 1
    download_size = speed * download_time
    print(f"Прошло {download_time} сек. Скачано {download_size} из {size} Мб ({round((download_size / size) * 100)}%)")
