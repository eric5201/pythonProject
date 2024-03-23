# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import sys
from toolkit.rename import AudioFileRename


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(sys.argv)
    AudioFileRename.audio_file_rename("./out/wlingf_skills_nlg.properties", "default", "./assets/tts")

    AudioFileRename.prefix_replace("./assets/tts", "test_")


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
