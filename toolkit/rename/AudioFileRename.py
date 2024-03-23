import os
import configparser


def audio_file_rename(audio_prop_file_path: str, language_name: str, audio_folder_path: str) -> None:
    properties = configparser.ConfigParser()
    properties.read(audio_prop_file_path)

    for filename in os.listdir(audio_folder_path):
        # 构造原始文件的完整路径
        src_file = os.path.join(audio_folder_path, filename)

        # 检查是否是文件而不是文件夹
        if os.path.isfile(src_file):
            # os.path.splitext函数返回一个包含两个元素的元组, 第一个元素是不带有后缀的文件名，第二个元素是文件的后缀名。忽略第二个返回值（使用_）来只获取不带后缀的文件名
            ori_name, _ = os.path.splitext(os.path.basename(src_file))
            print(ori_name)
            # # rsplit方法从字符串的末尾开始分割
            # ori_name2 = filename.rsplit('.', 1)[0]
            # print(ori_name2)

            for section in properties:
                if section != language_name:
                    continue
                for key, val in properties.items(section):
                    if val == ori_name:
                        # 构造新文件名
                        dest_file = os.path.join(audio_folder_path, key)

                        # 重命名文件
                        os.rename(src_file, dest_file)
                        print(f"文件 {filename} 已重命名为 {dest_file}")






def prefix_replace(folder_path, prefix):
    for filename in os.listdir(folder_path):
        # 构造原始文件的完整路径
        src_file = os.path.join(folder_path, filename)

        # 检查是否是文件而不是文件夹
        if os.path.isfile(src_file):
            new_file = filename.replace(prefix, "", 1)
            dest_file = os.path.join(folder_path, new_file)
            os.rename(src_file, dest_file)
            print(dest_file)
