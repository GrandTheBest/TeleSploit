import subprocess, cv2

def add_audio_to_video(original_video, processed_video, output_video):
    command = [
        "ffmpeg",
        "-i", processed_video,  # Входное обработанное видео (без звука)
        "-i", original_video,   # Оригинальное видео с аудио
        "-c:v", "copy",         # Оставляем видео без перекодирования
        "-c:a", "aac",          # Кодек для аудио
        "-strict", "experimental",
        "-map", "0:v:0",        # Берем видео из первого файла
        "-map", "1:a:0",        # Берем аудио из второго файла
        output_video
    ]
    subprocess.run(command, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

def crop_video_opencv(input_path, output_path, size=640):
    cap = cv2.VideoCapture(input_path)
    
    # Проверяем, открылось ли видео
    if not cap.isOpened():
        print("error!")
        return

    # Получаем размеры и FPS
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # Общее количество кадров

    # print(f"Source video: {width}x{height}, {fps} FPS, {frame_count} frames")

    # Определяем область обрезки
    min_dim = min(width, height)
    x_start = (width - min_dim) // 2
    y_start = (height - min_dim) // 2

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (size, size))

    frame_counter = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            # print(f"Success. Frames: {frame_counter}")
            break
        
        # Обрезаем и масштабируем
        cropped = frame[y_start:y_start+min_dim, x_start:x_start+min_dim]
        resized = cv2.resize(cropped, (size, size))
        
        out.write(resized)
        frame_counter += 1

    cap.release()
    out.release()