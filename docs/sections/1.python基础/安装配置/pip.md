## 一、安装 pip

### 1. 验证

如果使用的是 Python 3.4 或更高版本，`pip` 已经随 Python 安装在系统中。可以在终端或命令提示符中输入以下命令来验证 `pip` 是否已安装：

```bash
pip --version
```

如果输出显示版本信息，那么 `pip` 已经安装好了。

### 2. 安装

如果你的 Python 版本较旧或者没有安装 `pip`，可以下载 `get-pip.py` 脚本。在终端或命令提示符中输入以下命令：

```bash
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
```

或者如果你没有 `curl`，可以从浏览器下载：https://bootstrap.pypa.io/get-pip.py

然后，在终端或命令提示符中执行以下命令来安装 `pip`：

```bash
python get-pip.py
```

### 3. 更新 pip

在终端或命令提示符中执行以下命令来更新 `pip`：

```bash
pip install --upgrade pip
pip install -U pip
```

### 4. 显示 pip 的帮助信息

```bash
pip --help
```

## 二、配置 pip

使用镜像源有两种方式，以清华源为例：

### 1. 临时使用

```shell
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -U some-package
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple --trusted-host pypi.tuna.tsinghua.edu.cn/ some-package
```

除了`some-package`是要安装的库名外，其他都是固定格式

- ` -i`: 指定库的安装源
- `-U`:升级 原来已经安装的包，不带U不会装新版本，带上U才会更新到最新版本。
-  `--trusted-host` :添加信任网址


### 2. 设为默认

```shell
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple # 设置清华源
```

附`主流镜像源`地址

```bash
# 清华
https://pypi.tuna.tsinghua.edu.cn/simple
# 阿里云
http://mirrors.aliyun.com/pypi/simple/
# 豆瓣
http://pypi.douban.com/simple/
# 百度
https://mirror.baidu.com/pypi/simple
```

### 3. 创建pip链接

如果 `pip` 命令没有找到，但 `pip3` 可用，可以创建一个符号链接来将 `pip` 链接到 `pip3`

```bash
# Linux 和 macOS命令
sudo ln -s /usr/bin/pip3 /usr/bin/pip
```

## 三、pip基本操作

### 1. 安装包

```bash
pip install package_name

# 一次安装多个包
pip install package1 package2 ...

# 安装包的特定版本，可以使用等号来指定版本号
pip install package_name==version_number
```

### 2. 升级包

```bash
pip install --upgrade package_name
```

### 3. 卸载包

```bash
pip uninstall package_name
```

### 4. 列出已安装的包

 使用以下命令来列出已安装的所有包：

```bash
pip list
```

或者，如果你只想列出某一特定已安装包，可以使用：

```bash
pip show package_name
```

### 5. 创建 requirements 文件批量安装

你可以创建一个 `requirements.txt` 文件，列出你项目所需的所有包及其版本号。在文件中，每行写一个包及其版本号，例如：

```bash
numpy==1.19.5
pandas==1.3.2
matplotlib==3.4.3
```

然后，你可以使用以下命令从文件中安装所有包：

```bash
pip install -r requirements.txt
```

### 6. 导出Python包和库列表

使用pip可以将已安装的Python包和库列表导出到文件中，例如，使用以下命令将已安装的Python包和库列表导出到requirements.txt文件中：


```bash
pip freeze > requirements.txt
```

### 7. 查看需要升级的库

 目前已经安装的库中，看哪些需要版本升级

```shell
pip list -o
```

### 8. 检查兼容问题

 验证已安装的库是否有兼容依赖问题

```shell
pip check package-name
```

### 9. 下载库到本地

 将库下载到本地指定文件，保存为whl格式

```shell
pip download package_name -d "要保存的文件路径"
```

### 10. 清除pip安装缓存

```shell
pip cache purge
```

## 四、拓展

### 1. 使用第三方库`pipreqs`导出Python包和库列表

使用第三方库`pipreqs`生成项目的 `requirements.txt` 文件，`pipreqs`会分析项目中的 Python 源代码文件，找出所有依赖的包，并将它们及其版本写入 `requirements.txt` 文件。`pipreqs`可以只将用到的库生成到`requirements.txt`文件。

在终端中使用 pip 命令方法安装 ：

```text
pip install pipreqs
```

在当前目录使用`pipreqs`命令生成requirements.txt：

```text
pipreqs ./ --encoding=utf8  --force
```

- –encoding=utf8 ：为使用utf8编码
- –force ：强制执行，当生成目录下的requirements.txt存在时覆盖
- . /: 在哪个文件生成requirements.txt 文件