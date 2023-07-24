from PyQt5 import uic

fin = open('qt_Pityna.ui', 'r', encoding='utf-8')
fout = open('qt_PitynaUI.py', 'w', encoding='utf-8')
uic.compileUi(fin, fout)
fin.close()
fout.close()