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
    def check_exif(self, f):
        if f.lower().endswith('.jpg'):
            img = Image.open(self.path + f)
            info = img._getexif()
            if info != None:#if there is exif data continue
                if 36867 in info:
                    date = info[36867]
                    get_date = time.strptime(date, "%Y:%m:%d %H:%M:%S")
                    year = get_date[0]
                    month = get_date[1]
                    return self.path, f, year, month
                else:
                    pass
            else:
                pass
        else:
            pass


    def move_photos(self, path, filename, year, month):
        # if the path doesn't exist make the new directories and move file
        if os.path.isdir(self.move_to_path + str(year) + "/" + str(month) + "/") == False:
            os.makedirs(self.move_to_path + str(year) + "/" + str(month) + "/")
            shutil.move(path + filename, self.move_to_path + str(year) + "/" + str(month) + "/")
        #if the file already exists in the directory print a warning and skip file
        elif os.path.isfile(self.move_to_path + str(year) + "/" + str(month) + "/" + filename) == True:
            print(filename + " already exists in this directory")
            pass
        #all is good, file is being moved
        else:
            shutil.move(path + filename, self.move_to_path + str(year) + "/" + str(month) + "/")

def choose_destination():
    to_path = input('Enter Directory path to move photos to: ')
    save = input('Would you like to save this for future use? (this will overwrite any saved settings) ')
    if save.lower() == 'yes' or save.lower() == 'y':
        with open('move_to.txt', 'w') as move_it:
            move_it.write(to_path)
    return to_path

def saved_destination():
    if os.stat("move_to.txt").st_size != 0:
        with open('move_to.txt', 'r') as move_it:
            to_path = move_it.readline()
    else:
        print('You do not have a destination currently saved, please enter one...')
        choose_destination()
        pass
    return to_path


def main():

    menu_list = ["1. Choose Destination folder", "2. Use Saved Destination Folder"]
    for menu in menu_list:
        print(menu)
    choice = input("Choose an option: ")
    if choice == "1":
        to_path = choose_destination()
    elif choice == "2":
        to_path = saved_destination()
    else:
        print("Please select either 1 or 2")
        main()

    path = input('Enter Directory path that contains your photos to organize (this will NOT search subfolders!): ')

    photo = PhotoOrganizer(path, to_path)

    for f in os.listdir(path):
        if photo.check_exif(f) != None:
            p, filename, y, m = photo.check_exif(f)
            photo.move_photos(p, filename, y, m)

main()