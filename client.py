

import cv2
import numpy as np
import socket

# 创建UDP套接字
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# WSL的IP地址和端口号
wsl_address = ('172.21.246.1', 8888)

# 绑定套接字到WSL的地址和端口
sock.bind(wsl_address)

BUFFER_SIZE = 655070  # 数据包大小限制
print("connect success.")

while True:
    # 接收数据
    data, _ = sock.recvfrom(BUFFER_SIZE)
    print("Received:", len(data), "bytes")
    
    # 尝试将接收到的数据转换为图像
    try:
        frame = cv2.imdecode(np.frombuffer(data, dtype=np.uint8), cv2.IMREAD_COLOR)
        print("Decoded Image Size:", frame.shape)

        # 在WSL中显示图像
        cv2.imshow('Received Image', frame)
        if cv2.waitKey(1) == ord('q'):
            break
    except Exception as e:
        print("Error decoding image:", e)

# 关闭窗口
cv2.destroyAllWindows()
