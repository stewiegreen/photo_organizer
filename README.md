This is a Photo Organizing script I created on Python to help me learn.

It will ask you for the source directory for your photos then it will ask for
a destination directory.  The script looks at exif metadata and places your photos
into folders based on the month and year the photos were taken.

If the directory does not exist it will be created.
If the file is not a jpg, it will be skipped.
If the photo has no exif data it is skipped and is not moved.
If the photo already exists in that directory, it is not moved and terminal will
tell you which are duplicates (but terminal will not say which ones have no exif data).

The file structure ends up looking like this:
Destination folder/year/month/

Some things to do:

Set up a simple .txt file that sets a permanent root folder location where all photos are saved.

Add an option to rename photos (something like YY_MM_DD_HH_MM_SS.jpg) so that they are in
chronological order no matter how many friends/family you get your photos from

Add more photo types
