import subprocess
import json

def check_video_quality(file_path):
    # 构造 ffprobe 命令，提取宽、高和时长
    cmd = [
        'ffprobe',
        '-v', 'quiet',
        '-print_format', 'json',
        '-show_entries', 'stream=width,height, codec_type',
        '-show_entries', 'format=duration',
        file_path
    ]
    
    try:
        # 执行命令并获取输出
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        data = json.loads(result.stdout)
        
        # 解析数据
        video_stream = next((s for s in data['streams'] if s['codec_type'] == 'video'), None)
        duration = float(data['format']['duration'])
        
        if video_stream:
            width = video_stream['width']
            height = video_stream['height']
            print(f"视频分辨率: {width}x{height}, 时长: {duration:.2f}秒")
            
            # 业务逻辑判断
            if width >= 1280 and height >= 720 and duration > 30:
                print("✅ 判定结果：该视频属于高清长视频。")
            else:
                print("❌ 判定结果：该视频不符合高清长视频标准。")
        else:
            print("未找到视频流信息。")
            
    except Exception as e:
        print(f"执行出错: {e}")

# 替换成你的本地文件路径进行练习
check_video_quality('BigBuckBunny_640x360.avi')