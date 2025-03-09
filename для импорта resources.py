import os

# Путь к папке с файлами
folder_path = "Images"
# Имя выходного .qrc файла
qrc_file = "resources.qrc"

# Открываем .qrc файл для записи
with open(qrc_file, "w", encoding="utf-8") as f:
    f.write('<RCC>\n')
    f.write('    <qresource prefix="/">\n')

    # Рекурсивно добавляем все файлы из папки
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            relative_path = os.path.relpath(file_path, start=os.path.dirname(qrc_file))
            f.write(f'        <file>{relative_path.replace("\\", "/")}</file>\n')

    f.write('    </qresource>\n')
    f.write('</RCC>\n')

print(f"Файл {qrc_file} успешно создан.")