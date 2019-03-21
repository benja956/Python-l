#BatchInstall.py
import os
libs = {"numpy","matplotlib","pillow","sklearn","requests",\
        "jieba","beautifulsoup4","wheel","networkx","sympy",\
        "pyinstaller","django","flask","werobot","pyqt5",\
        "pandas","pyopengl","pypdf2","docopt","pygame","turtle","pkyseg"}
try:
    for lib in libs:
        os.system("pip3 install "+lib)
    print("Successful")        
except:
    print("Failed Somehow")
