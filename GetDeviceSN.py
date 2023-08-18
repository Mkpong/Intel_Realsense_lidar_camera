import pyrealsense2 as rs

# 리얼센스 컨텍스트 초기화
context = rs.context()

# 연결된 기기 목록 가져오기
devices = context.query_devices()

for device in devices:
    print(f"Device Name: {device.get_info(rs.camera_info.name)}")
    print(f"Serial Number: {device.get_info(rs.camera_info.serial_number)}")
    print("-" * 30)