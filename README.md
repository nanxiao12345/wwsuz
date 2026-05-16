# wwsuz 
**practice using ffmpeg command**

## FFmpeg plan list
1. [x] Basic transcode
2. [x] Probe media information(尝试理解输出的分辨率 、码率、编码格式等信息)
3. [] Grasp encoder control(学会手动指定编码器，理解不同编码器的区别。)
    - Check encoder
    - Designed video encoder transcoding
    - Designed audio encoder
4. [] Viedo cropping and scaling(掌握视频的时间和空间裁剪技能)
    - Time croppng
    - Aspect rate scaling
    - Combination operation
5. [] Audio and video separation and extraction(学会从视频中提取音频，或将音视频合并。)
    - Audio Extraction
    - Extract audio and convert  format
    - Extract video without sound 
    - Merge audio and video
6. [] FFplay exploration
7. [] 复盘 + 综合练习(独立完成下述5步，并在不查资料的情况下解释每个参数的含义)
    - 查看该视频的编码信息（使用ffprobe）
    - 截取视频的第10-20秒片段
    - 将该片段缩放到640x360分辨率
    - 提取该片段的音频保存为MP3
    - 用FFplay预览最终结果
8. [] 滤镜应用（水印、字幕、GIF）-- 学会使用滤镜给视频添加特效
    - 添加文字水印
    - 添加图片水印
    - 视频转GIF
    - 多滤镜组合（缩放+水印）
9. [] 截图与缩略图
    - 单帧截图（指定时间点）
    - 连续截图（每秒一帧）
    - 生成缩略图网格（视频预览图）
    - 高质量截图
    ------
    小练习：为一个长视频生成9宫格缩略图（类似视频网站的预览功能）。
10. [] 批量处理与脚本化
11. [] 制作一个“视频处理工具箱”脚本
    - 接收一个视频文件路径作为输入
    - 显示视频的详细信息（分辨率、时长、编码格式）
    - 询问用户想要什么操作\
        1. 选项1：转换为720p MP4
        2. 选项2：提取音频为MP3
        3. 选项3：裁剪前30秒
        4. 选项4：生成缩略图网格
    - 根据用户选择执行相应操作