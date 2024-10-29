itera = 1
import time
print("before")
706: ˂
707: ˃
708: ˄
709: ˅

1998: ߎ
1999: ߏ
1421: ֍
1422: ֎
while True:
	input()
	while True:
		print(f"{itera}: {chr(itera)}")
		itera +=1
		time.sleep(.05)
		if itera % 1000 == 0:
			break
input('type anything then press enter to go on')
print('watch the magic')
def instant():
    import sys, termios

    fd = sys.stdin.fileno()
    orig = termios.tcgetattr(fd)

    new = termios.tcgetattr(fd)
    new[3] = new[3] & ~termios.ICANON
    new[6][termios.VMIN] = 1
    new[6][termios.VTIME] = 0

    try:
        termios.tcsetattr(fd, termios.TCSAFLUSH, new)
        return sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSAFLUSH, orig)
while True:
	print('', end='', flush=True)
	c = instant()
	print()
	if c == 'w':
		print('up')
	elif c == 'a':
		print('left')
	elif c == 's':
		print('down')
	elif c == 'd':
		print('right')
	elif c == '@':
		print("le")
