import pyrealsense2 as rs
import numpy as np
import cv2
import math

# 파이프라인 초기화
pipeline = rs.pipeline()
config = rs.config()
config.enable_device("f0246287")  # Replace with your device serial number
config.enable_stream(rs.stream.color, 640, 480, rs.format.rgb8, 30)
config.enable_stream(rs.stream.accel) 

# 파이프라인 시작
pipeline.start(config)

image_count = 0
try:
    while True:
        # 프레임 가져오기
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        if not color_frame:
            continue

        color_image = np.asanyarray(color_frame.get_data())
        color_image = cv2.cvtColor(color_image, cv2.COLOR_BGR2RGB)

        # 화면에 표시
        cv2.imshow("Camera", color_image)

        # 's' 키를 누르면 사진 찍기
        key = cv2.waitKey(1) & 0xFF
        if key == ord('s'):
            # 좌표계 파일 저장
            accel_frames = pipeline.wait_for_frames()
            accel_frame = accel_frames.first_or_default(rs.stream.accel)
            accel_data = accel_frame.as_motion_frame().get_motion_data()
            
            accel_data_x_deg = math.degrees(math.atan(accel_data.x))
            accel_data_y_deg = math.degrees(math.atan(accel_data.y))
            accel_data_z_deg = math.degrees(math.atan(accel_data.z))

            save_path_accel = f"./Captured_Image/accel_data/accel_data_{image_count:06d}.txt"

            print(f"Accel X: {accel_data_x_deg:.2f}°, Accel Y: {accel_data_y_deg:.2f}°, Accel Z: {accel_data_z_deg:.2f}°")

            with open(save_path_accel , "w") as f:
                f.write(f"{accel_data_x_deg} {accel_data_y_deg} {accel_data_z_deg}")

            save_path_image = f"./Captured_Image/captured_image_{image_count:03d}.jpg"
            cv2.imwrite(save_path_image, color_image)
            print("Image captured! ( image_count )")
            image_count += 1

        # 'q' 키를 누르면 종료
        if key == ord('q'):
            break

finally:
    # 파이프라인 종료
    pipeline.stop()

    # OpenCV 창 닫기
    cv2.destroyAllWindows()
