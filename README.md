This is a Photo Organizing script I created on Python to help me learn.

It will give you 2 menu options and then ask you for the source directory for your photos and the
destination directory.  The script looks at exif metadata and places your photos into folders based 
on the month and year the photos were taken.

If the destination directory does not exist it will be created.
If the file is not a jpg, it will be skipped.
If the photo has no exif data it is skipped and is not moved.
If the photo already exists in that directory, it is not moved and terminal will tell you which are 
duplicates (but terminal will not say which ones have no exif data).

The file structure ends up looking like this:
Destination folder/year/month/

Some things to do:

Make the code more readable.

Add more photo types

I've decided not to have a rename option because there are really no good - batch auto renaming - solutions.
