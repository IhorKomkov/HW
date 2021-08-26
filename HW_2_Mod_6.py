"""sort the files in folder script"""
import shutil
import sys
from pathlib import Path
import re


"""lists for file nemes out"""
# images
IMG = []
# video
VID = []
# documents
DOC = []
# audio
MUZ = []
# archives
ARCH = []
#unknown
UNKNOWN = []

"""known formats"""
# images extension
img_ext = ['.jpeg', '.jpg','.png','.svg']
# video extension
vid_ext = ['.avi', '.mp4', '.mov', '.mkv', '.mp4']
# documents extension
doc_ext = ['.doc', '.docx', '.txt', '.pdf', '.xlsx', '.pptx']
# audio extension
aud_ext = ['.mp3', '.ogg', '.wav', '.amr', '.m4a']
# archives extension
arch_ext = ['.zip', '.gz', '.tar', '.7z']
# unknown extension
unw_ext = set()
# known extension
nwn_ext = set()

"""folders for sort"""
our_folders = ['archives', 'video', 'audio', 'documents', 'images']


def folders_create(path):
    """create target folders"""
    for i in our_folders:
        Path(path + '/' + i).mkdir(exist_ok=True)


def scan_f(path):
    """scan in folder func"""
    for i in Path(path).iterdir():
        if i.suffix.lower() in img_ext: # if suffix is in known formats
            IMG.append(i.name) #add filename to file list for return
            nwn_ext.add(i.suffix.lower()) # add suffix to known formats list
            i.replace(path + '/' + 'images')
        elif i.suffix.lower() in vid_ext:
            VID.append(i.name)
            nwn_ext.add(i.suffix.lower())
        elif i.suffix.lower() in doc_ext:
            DOC.append(i.name)
            nwn_ext.add(i.suffix.lower())
        elif i.suffix.lower() in aud_ext:
            MUZ.append(normalize(i.stem) + i.suffix)
            nwn_ext.add(i.suffix.lower())
        elif i.suffix.lower() in arch_ext:
            ARCH.append(i.name)
            nwn_ext.add(i.suffix.lower())
        elif i.is_dir(): # scan in subfolders - recursion
            if i.name in our_folders: # if our folder - skip it
                continue
            else:
                scan_f(str(i))
        else:
            unw_ext.add(i.suffix) # add suffix to unknown formats list
    return IMG, VID, DOC, MUZ, ARCH, nwn_ext, unw_ext # all lists of sorted files, filnames + known extentions + unknown extentions


"""dictionary for transliteration"""
CYRILLIC_SYMBOLS = "абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ"
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l",
                "m", "n", "o", "p", "r", "s", "t", "u", "f", "h", "ts", "ch",
                "sh", "sch", "", "y", "", "e", "yu", "u", "ja", "je", "ji", "g")
TRANS = {}
j = 0
for i in CYRILLIC_SYMBOLS:
    TRANS[i] = TRANSLATION[j]
    j += 1

for c, l in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(c)] = l
    TRANS[ord(c.upper())] = l.upper()

def normalize(f_name):
    return re.sub(r'\W', '_', f_name.translate(TRANS))




print(folders_create('C:\\Users\IHORKOMKOV\Desktop\разобрать'), scan_f('C:\\Users\IHORKOMKOV\Desktop\разобрать'))

# def main():
#     folders_create(path)
#     print(scan_f(path))
#
#
# if __name__ == "__main__":
#     path = sys.argv[1]
#     main()
