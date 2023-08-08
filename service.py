import cv2
import numpy as np
import socket
import time

# 创建UDP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# WSL虚拟机的IP地址和端口号
wsl_address = ('172.21.246.1', 8888)

# 启动摄像头
cap = cv2.VideoCapture(0)

BUFFER_SIZE = 65507  # 数据包大小限制

while True:
    ret, frame = cap.read()  # 读取摄像头帧
    if not ret:
        break

    # 将图像转换为字符串
    _, img_encoded = cv2.imencode('.jpg', frame)
    img_bytes = np.array(img_encoded).tobytes()

    # 分段发送数据到WSL
    for i in range(0, len(img_bytes), BUFFER_SIZE):
        data = img_bytes[i : i + BUFFER_SIZE]
        sock.sendto(data, wsl_address)
        print("Sent:", len(data), "bytes")

    # 在Windows中显示摄像头画面
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

    # 控制发送帧率为15帧每秒
    time.sleep(1/15)

# 关闭摄像头和窗口
cap.release()
cv2.destroyAllWindows()


# 启动摄像头
cap = cv2.VideoCapture(0)

BUFFER_SIZE = 131014  # 65507,数据包大小限制

while True:
    ret, frame = cap.read()  # 读取摄像头帧
    if not ret:
        break

    # 将图像转换为字符串
    _, img_encoded = cv2.imencode('.jpg', frame)
    img_bytes = np.array(img_encoded).tobytes()

    # 分段发送数据到WSL
    for i in range(0, len(img_bytes), BUFFER_SIZE):
        data = img_bytes[i : i + BUFFER_SIZE]
        sock.sendto(data, wsl_address)
        print("Sent:", len(data), "bytes")

    # 在Windows中显示摄像头画面
    cv2.imshow('Camera', frame)
    if cv2.waitKey(1) == ord('q'):
        break

# 关闭摄像头和窗口
cap.release()
cv2.destroyAllWindows()
