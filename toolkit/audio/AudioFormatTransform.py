
import subprocess
import ffmpeg
import os



def wav_to_pcm_by_py_ffmpeg(wav_file, audio_hz):
    wav_file_name, wav_suffix = os.path.splitext(os.path.basename(wav_file))
    if wav_suffix == '.wav':
        abs_path = os.path.abspath(wav_file)
        root_dir, _ = os.path.split(abs_path)
        output_file = root_dir + "/" + wav_file_name + '.pcm'
        # 构建转换命令:
        # -i "{input_wav_file}"：指定输入文件。
        # -f s16le：指定输出格式为有符号16位小端格式，这是PCM数据的一种常见格式。
        # -ar 44100：设置音频的采样率为44.1kHz。你可以根据需要更改这个值。
        # -ac 2：设置音频通道为立体声。如果你的音频是单声道，将其更改为-ac 1。
        # "{output_pcm_file}"：指定输出文件。
        command = f'{ffmpeg} -i "{wav_file}" -f s16le -ar {audio_hz} -ac 1 "{output_file}"'
        # 执行转换命令
        stdout, stderr = ffmpeg.run(command, capture_stdout=True, capture_stderr=True)
        print("stdout: ", stdout + "\nstderr: ", stderr + "")



def wav_to_pcm_by_ffmpeg_cmd(wav_file, audio_hz):
    wav_file_name, wav_suffix = os.path.splitext(os.path.basename(wav_file))
    if wav_suffix == '.wav':
        abs_path = os.path.abspath(wav_file)
        root_dir, _ = os.path.split(abs_path)
        output_file = root_dir + "/" + wav_file_name + '.pcm'

        # 构建FFmpeg命令
        ffmpeg_command = f'ffmpeg -i "{wav_file}" -ar {audio_hz} -f s16le -acodec pcm "{output_file}"'

        # 执行FFmpeg命令
        subprocess.run(ffmpeg_command, shell=True)


def wav_to_pcm(wav_file, audio_hz):
    wav_file_name, wav_suffix = os.path.splitext(os.path.basename(wav_file))
    if wav_suffix == '.wav':
        abs_path = os.path.abspath(wav_file)
        root_dir, _ = os.path.split(abs_path)
        output_file = root_dir + "/" + wav_file_name + '.pcm'

        # 构建转换命令
        command = [
            'ffmpeg',
            '-i', wav_file,
            '-f', 's16le',
            '-acodec', 'pcm_s16le',
            '-ar', audio_hz,  # 设置采样率
            '-ac', '2',  # 设置通道数，单声道为'1'
            output_file
        ]

        # 执行转换命令
        process = ffmpeg.run(command, capture_output=True)

        # 检查命令执行结果
        if process.returncode == 0:
            print("转换成功。")
        else:
            print("转换失败，错误信息：", process.stderr.decode())
