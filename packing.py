import os
import zipfile

def zip_all_except_specific_items(zipf, items_to_exclude):
    for root, dirs, files in os.walk('.'):
        for item in items_to_exclude:
            if item in dirs:
                dirs.remove(item) 
        for file in files:
            if file not in items_to_exclude:
                zipf.write(os.path.join(root, file),
                           os.path.relpath(os.path.join(root, file)))

zip_file_name = 'Modpack-Translation-Zack.zip'
items_to_exclude = [os.path.basename(__file__), zip_file_name]
items_to_exclude.extend(['.git', '.gitignore', '.github', 'README.md', 'LICENSE', 'crowdin.yml']) 

with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    zip_all_except_specific_items(zipf, items_to_exclude)
