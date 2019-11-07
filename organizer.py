import os
import os.path
import shutil
from PIL import Image
import time


class PhotoOrganizer:
    def __init__(self, path, move_to_path):
        self.path = path
        self.move_to_path = move_to_path

#checks exif data
    def check_exif(self):
        file = []
        for f in os.listdir(self.path):
            if f.lower().endswith('.jpg'):
                img = Image.open(self.path + f)
                info = img._getexif()
                if info:#if there is exif data continue
                    if 36867 in info:
                        date = info[36867]
                        get_date = time.strptime(date, "%Y:%m:%d %H:%M:%S")
                        year = get_date[0]
                        month = get_date[1]
                        file.append([self.path, f, year, month])
        return file


    def move_photos(self, file):
        for f in file:
            p = f[0]
            filename = f[1]
            y = f[2]
            m = f[3]

            if os.path.isdir(self.move_to_path + str(y) + "/" + str(m) + "/") == False:
                os.makedirs(self.move_to_path + str(y) + "/" + str(m) + "/")
                shutil.move(p + filename, self.move_to_path + str(y) + "/" + str(m) + "/")
            elif os.path.isfile(self.move_to_path + str(y) + "/" + str(m) + "/" + filename) == True:
                print(filename + " already exists in this directory")
                pass
            else:
                shutil.move(p + filename, self.move_to_path + str(y) + "/" + str(m) + "/")





folder = input('Enter Directory path to Search (this will NOT search subfolders!): ')
to_folder = input('Enter Directory path to move photos to: ')


photo = PhotoOrganizer(folder, to_folder)

photo.move_photos(photo.check_exif())
