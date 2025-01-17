# Already happens to you?
<div align="justify">
I had an SD card in my old car with music that I had chosen from my personal collection on my NAS. I bought a new car but it didn't have an SD card reader, only have USB ports. Furthermore, some files on the SD card were corrupt and I'm getting read errors, so it was not possible to copy the files from the SD card to a PEN Drive. In addition to this, the folder structure on the SD card was different from that on the NAS and it did not have the image files for the album covers. The only solution would be to re-copy and organize all files from the NAS collection. This had already happened when the SD card get corrupted. So, I rolled up my sleeves and I create this script that collects the list of files on the SD card, searches the NAS for the same songs and copies the songs from the NAS to the same folder structure on a destination, for example a PEN Drive. Additionally, the script creates a json with list of source files, you can use the script to rebuild your music collection after formatting a corrupted SD card or PEN Drive.

<br>

# Using the script.
## Configuration

Open the script in some editor (e.g. Visual Studio Code or Notepad++) and configure the following variables:

* <strong>OLD_LOCATION</strong> (string): the path to the old location of the files (e.g. my SD Card)
* <strong>NEW_LOCATION</strong> (string): the path to the new location of the files (e.g. my new PEN Drive)
* <strong>SOURCE_LOCATIONS</strong> (list o strings): a list of locations (paths) from where to copy the original files (e.g a bunch of folders in my NAS)

## Running the script
If you are using an IDE like the VS Code you can run the script directly from the IDE.

### Running from the command line
* Open a terminal on Mac/Linux or a command shell in Windows
* Use de cd command and go to the script directory
* Run the script

```
python get_my_music_back.py
```
* The script will ask you if you want to start the copy, you can do one of two things:
    
    - If you are rebuilding a corrupted device, type "no" and press enter. Then format de device and run the script again. The old files references are saved in the <strong>old_files.json</strong> file, the script will use it to retrieve the files from the SOURCE_LOCATIONS to the NEW_LOCATION. In this case, the OLD_LOCATION and the NEW_LOCATION are the same, paid attention to the new mount point after formatting the device and modify the NEW_LOCATION variable if needed.
    - If you are just creating a collection of music in a new location just press enter.

## About the JSON files
There are two json files that are created in the script directory:
* <strong>old_files.json</strong>: this file contains the result of the OLD_LOCATION files scanned. Delete this file if you need to scan a OLD_LOCATION again (e.g new files added from the last time you used the script or the device is not the same and have a new collection of music).
* <strong>source_files.json</strong>: this file contains the result of the SOURCE_LOCATIONS files scanned. Delete this file to re-scan the SOURCE_LOCATIONS again.

# Other uses
The script was created to solve my problem, related with my car music collection, but can be used for other type of files. Just change the MIMES variable to accomplish that.

</div>
