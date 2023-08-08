<!DOCTYPE html>
<html>
</head>
<body>
  <h1>Use Camera On WSL</h1>

  <p>这是一个使用OpenCV和Socket库，在Windows中读取相机实时图像流并通过UDP套接字传输到WSL进行可视化的项目。</p>

  <h2>功能</h2>
  <ul>
    <li>从相机或摄像头中捕获实时图像流。</li>
    <li>使用UDP套接字将图像数据传输到WSL。</li>
    <li>在WSL中使用OpenCV进行图像处理和可视化展示。</li>
  </ul>

  <h2>环境要求</h2>
  <ul>
    <li>Windows操作系统</li>
    <li>WSL (Windows Subsystem for Linux)</li>
    <li>Python 3.x</li>
    <li>OpenCV库</li>
    <li>Socket库</li>
  </ul>

  <h2>安装步骤</h2>
  <ol>
    <li>克隆本仓库到本地计算机。</li>
    <li>在Windows和WSL中安装Python 3.x、OpenCV、Socket。</li>
    <li>将server.py复制到Windows中，并运行：</li>
    <pre><code>python ./server.py</code></pre>
    <li>将client复制到WSL中，并运行：</li>
    <pre><code>python ./client.py</code></pre>
    <li>程序将开始读取相机的实时图像流，并通过UDP套接字传输到WSL进行可视化展示。</li>
  </ol>

  <h2>注意事项</h2>
  <ul>
    <li>确保ip配置正确，server与client的address应均为WSL的ip。</li>
    <li>确保端口一致。</li>
  </ul>

  <h2>作者</h2>
  <ul>
    <li>作者：Louxudoong</li>
    <li>邮箱：867131085@qq.com</li>
  </ul>
</body>
</html>
