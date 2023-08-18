import cv2

# 비디오 파일 열기
video_path = 'output4.avi'
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Could not open video file.")
    exit()

# 비디오 정보 가져오기
fps = int(cap.get(cv2.CAP_PROP_FPS))
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

print(int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))

# 프레임 추출 및 저장
frame_number = 0
while True:
    ret, frame = cap.read()
    print(ret)
    print(frame)
    if not ret:
        break

    frame_filename = f"./FrameFolder/1280x720/output4/frame_{frame_number:04d}.jpg"
    cv2.imwrite(frame_filename, frame)

    frame_number += 1

    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 비디오 파일 닫기
cap.release()
cv2.destroyAllWindows()