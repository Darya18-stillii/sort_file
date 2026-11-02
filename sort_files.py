import os
import shutil
SORTING_RULES = {
    'images': ['.jpg', '.png', '.gif'],
    'documents': ['.pdf','.docx','.txt'],
    'music': ['.mp3']
}

def get_category(ext):
    for folder, extension in SORTING_RULES.items():
        if ext in extension:
            return folder
    return 'other'
def sort_folder (folder):
    files = os.listdir(folder)
    for file in files:
        full_path = os.path.join(folder,file)
        if os.path.isdir(full_path):
            continue
        else:
            name, ext = os.path.splitext(file)
            ext = ext.lower()
            category = get_category(ext)
            dest_folder = os.path.join(folder,category)
            if not os.path.exists(dest_folder):
                os.makedirs(dest_folder)
            try:
                shutil.move(full_path, os.path.join(dest_folder,file))
                print(f'Перемещен: {file} -> {category}')
            except Exception as e:
                print(f'Ошибка: {e}')




