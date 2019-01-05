from pykeyboard import *

k = PyKeyboard()

k.type_string(u'杀毒防御')  # 我靠不能输入中文啊。。。
k.press_key('H')  # 模拟键盘按H键
k.release_key('H')  # 模拟键盘松开H键
k.tap_key('H')  # 模拟点击H键

k.tap_key('H', n=2, interval=5)  # 模拟点击H键，2次，每次间隔5秒
k.tap_key(k.function_keys[5])  # 点击功能键F5

# 组合键模拟
# 例如同时按alt+tab键盘
k.press_key(k.alt_key)  # 按住alt键
k.tap_key(k.tab_key)  # 点击tab键
k.release_key(k.alt_key)  # 松开alt键