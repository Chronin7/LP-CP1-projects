itera = 1
import time
print("before")
def leomb():
	'''706: ˂
	707: ˃
	708: ˄
	709: ˅
	ඞ
	3980: ྌ
	3981: ྍ
	3982: ྎ
	3983: ྏ
	3984: ྐ
	3985: ྑ
	3986: ྒ
	3987: ྒྷ
	3988: ྔ
	3989: ྕ
	3990: ྖ
	3991: ྗ
	3992: ྘
	3993: ྙ
	3994: ྚ
	3995: ྛ
	3996: ྜ
	3997: ྜྷ
	3998: ྞ
	3999: ྟ

	4000: ྠ
	4001: ྡ
	4002: ྡྷ
	4003: ྣ
	4004: ྤ
	4005: ྥ
	4006: ྦ
	4007: ྦྷ
	4008: ྨ
	4009: ྩ
	4010: ྪ
	4011: ྫ
	4012: ྫྷ
	4013: ྭ
	4014: ྮ
	4015: ྯ
	4016: ྰ
	4017: ྱ
	4018: ྲ
	4019: ླ
	4020: ྴ
	4021: ྵ
	4022: ྶ
	4023: ྷ
	4024: ྸ
	4025: ྐྵ
	4026: ྺ
	4027: ྻ
	4028: ྼ
	1998: ߎ
	1999: ߏ
	1421: ֍
	1422: ֎'''
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
