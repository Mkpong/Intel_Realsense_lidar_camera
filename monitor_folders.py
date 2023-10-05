import os
import time

# 0번 카메라 폴더를 스캔하면서 1,2,3,4,5번 카메라에 해당 이미지가 한 폴더에라도 없으면 0번 카메라 폴더에서 해당 이미지를 삭제
def monitor_folder(folders):
    # 파일 생성
    files = []
    for folder in folders:
        files.append(sorted(os.listdir(folder)))
    
    # 한 폴더의 파일을 스캔하면서 나머지 폴더에 해당 파일의 이름이 없다면 삭제
    for i in range(len(folders)):
        for filename in files[i]:
            for j in range(len(folders)):
                if filename not in files[j]:
                    # 해당 폴더 경로 삭제
                    image_path = os.path.join(folders[i], filename)
                    try:
                        os.remove(image_path)
                        print(image_path , "파일 삭제")
                    except OSError as e:
                        print("파일을 삭제할 수 없습니다." , e)
                    break


camera01 = "./test1"
camera02 = "./test2"
camera03 = "./test3"
# camera04 = "./test4"
# camera05 = "./test5"
# camera06 = "./test6"
folder_paths = [camera01, camera02, camera03]


monitor_folder(folder_paths)

