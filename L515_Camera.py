import pyrealsense2 as rs
import numpy as np
import cv2

# 파이프라인 초기화
pipeline = rs.pipeline()
config = rs.config()
config.enable_device("f0244988")
config.enable_stream(rs.stream.color, 1280, 720, rs.format.rgb8, 30)

pipeline2 = rs.pipeline()
config2 = rs.config()
config2.enable_device("f0232277")
config2.enable_stream(rs.stream.color, 1280, 720, rs.format.rgb8, 30)

pipeline3 = rs.pipeline()
config3 = rs.config()
config3.enable_device("f0246287")
config3.enable_stream(rs.stream.color, 1280, 720, rs.format.rgb8, 30)

pipeline4 = rs.pipeline()
config4 = rs.config()
config4.enable_device("f0232056")
config4.enable_stream(rs.stream.color, 1280, 720, rs.format.rgb8, 30)

# 파이프라인 시작
pipeline.start(config)
pipeline2.start(config2)
pipeline3.start(config3)
pipeline4.start(config4)

# 녹화 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 30.0, (1280, 720))

fourcc2 = cv2.VideoWriter_fourcc(*'XVID')
out2 = cv2.VideoWriter('output2.avi', fourcc2, 30.0, (1280, 720))

fourcc3 = cv2.VideoWriter_fourcc(*'XVID')
out3 = cv2.VideoWriter('output3.avi', fourcc3, 30.0, (1280, 720))

fourcc4 = cv2.VideoWriter_fourcc(*'XVID')
out4 = cv2.VideoWriter('output4.avi', fourcc4, 30.0, (1280, 720))

try:
    while True:
        # 프레임 가져오기
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()

        frames2 = pipeline2.wait_for_frames()
        color_frame2 = frames2.get_color_frame()

        frame3 = pipeline3.wait_for_frames()
        color_frame3 = frame3.get_color_frame()

        frame4 = pipeline4.wait_for_frames()
        color_frame4 = frame4.get_color_frame()

        if not color_frame or not color_frame2 or not color_frame3 or not color_frame4:
            continue

        # 이미지 데이터 추출
        color_image1 = np.asanyarray(color_frame.get_data())
        color_image2 = np.asanyarray(color_frame2.get_data())
        color_image3 = np.asanyarray(color_frame3.get_data())
        color_image4 = np.asanyarray(color_frame4.get_data())
        
        color_image1 = cv2.cvtColor(color_image1 , cv2.COLOR_BGR2RGB)
        color_image2 = cv2.cvtColor(color_image2 , cv2.COLOR_BGR2RGB)
        color_image3 = cv2.cvtColor(color_image3 , cv2.COLOR_BGR2RGB)
        color_image4 = cv2.cvtColor(color_image4 , cv2.COLOR_BGR2RGB)

        # 화면에 표시
        cv2.imshow("Camera1", color_image1)
        cv2.imshow("Camera2" , color_image2)
        cv2.imshow("Camera3" , color_image3)
        cv2.imshow("Camera4" , color_image4)
        
        # 비디오로 저장
        out.write(color_image1)
        out2.write(color_image2)
        out3.write(color_image3)
        out4.write(color_image4)
        
        # 'q' 키를 누르면 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # 파이프라인 종료
    pipeline.stop()
    pipeline2.stop()
    pipeline3.stop()
    pipeline4.stop()

    # 비디오 녹화 종료
    out.release()
    out2.release()
    out3.release()
    out4.release()

# OpenCV 창 닫기
cv2.destroyAllWindows()