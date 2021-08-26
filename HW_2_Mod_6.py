# У многих на рабочем столе есть папка, которая называется как-то вроде
# "Разобрать". Как правило, разобрать эту папку руки никогда так и не доходят.
#
# Мы с вами напишем скрипт, который разберет эту папку. В конечном итоге вы
# сможете настроить эту программу под себя и она будет выполнять индивидуальный
# сценарий соответствующий вашим нуждам. Для этого наше приложение будет
# проверять расширение файла (последние символы в имени файла, как правило
# после точки) и в зависимости от расширения принимать решение к какой
# категории отнести этот файл.
#
# Скрипт принимает один аргумент при запуске — это имя папки в которой он
# будет проводить сортировку. Допустим файл с программой называется sort.py,
# тогда чтобы отсортировать папку /user/Desktop/Хлам надо запустить скрипт
# командой python sort.py /user/Desktop/Хлам
#
#     Для того, чтобы успешно справится с этим заданием вы должны вынести 
#     логику обработки папки в отдельную функцию.
#     Чтобы скрипт мог пройти на любую глубину вложенности, функция обработки
#     папок должна рекурсивно вызывать сама себя когда ей встречаются вложенные
#     папки.
#
# Скрипт должен проходить по указанной во время вызова папке и сортировать все
# файлы по группам:
#
#     изображения ('JPEG', 'PNG', 'JPG', 'SVG');
#     видео файлы ('AVI', 'MP4', 'MOV', 'MKV');
#     документы ('DOC', 'DOCX', 'TXT', 'PDF', 'XLSX', 'PPTX');
#     музыка ('MP3', 'OGG', 'WAV', 'AMR');
#     архивы ('ZIP', 'GZ', 'TAR');
#     неизвестные расширения.
#
# Вы можете расширить и дополнить этот список если хотите.
#
# В результатах работы должны быть:
#
#     Список файлов в каждой категории (музыка, видео, фото и пр.)
#     Перечень всех известных скрипту расширений, которые встречаются в целевой
#     папке.
#     Перечень всех расширений, которые скрипту неизвестны.
#
# После необходимо добавить функции, которые будут отвечать за обработку каждого
# типа файлов.
#
# Кроме того, все файлы и папки нужно переименовать, удалив из названия все
# потенциально приводящие к проблемам символы. Для этого надо применить к
# именам файлов функцию normalize. Следует помнить, что переименовать файлы
# нужно так, чтобы не изменить расширения файлов.
#
# Функция normalize:
#
#     Проводит транслитерацию кириллического алфавита на латинский.
#     Заменяет все символы кроме латинских букв, цифр на '_'.
#
# Требования к функции normalize:
#
#     принимает на вход строку и возвращает строку;
#     проводит транслитерацию кириллических символов на латиницу;
#     заменяет все символы кроме букв латинского алфавита и цифр на символ '_';
#     транслитерация может не соответствовать стандарту, но быть читабельной;
#     большие буквы остаются большими, а меленькие -- маленькими после транслитерации.
#
# Условия для обработки:#
#
#     изображения переносим в папку images
#     документы переносим в папку documents
#     аудио файлы переносим в audio
#     видео файлы в video
#     архивы распаковываются и их содержимое переносится в папку archives
#
# Критерии приёма задания#
#
#     все файлы и папки переименовываются при помощи функции normalize.
#     расширения файлов не изменяются после переименования.
#     пустые папки удаляются
#     скрипт игнорирует папки archives, video, audio, documents, images;
#     распакованное содержимое архива переносится в папку archives в подпапку
#     названную точно так же, как и архив, но без расширения в конце;
#     файлы, расширения которых не известны, остаются без изменений.


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
