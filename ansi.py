import os
os.system('color')

CSI = f"{chr(27)}["

def fg(rgb):
	r = int(rgb[0:2], 16)
	g = int(rgb[2:4], 16)
	b = int(rgb[4:6], 16)
	freecol = f"38;2;{r};{g};{b}"
	return freecol
def bg(rgb):
	r = int(rgb[0:2], 16)
	g = int(rgb[2:4], 16)
	b = int(rgb[4:6], 16)
	freecol = f"48;2;{r};{g};{b}"
	return freecol
def clearscreen():
	print(f"{CSI}2J")
	print(f"{CSI}0;0H")

clearscreen()
print(f"{CSI}{fg('BB00FF')};{bg('440088')}mText{CSI}0m")
print(f"{CSI}41;36mText2{CSI}0m")
for i in range(0,8):
    print(i, f"{CSI}3{i}m●{CSI}0m", f"{CSI}3{i};1m●{CSI}0m")
print("Traffic lights")
redOn = f"{CSI}{fg('FF0000')}m●{CSI}0m"
redOff = f"{CSI}{fg('660000')}m●{CSI}0m"
print(redOn, redOff)
yellowOn = f"{CSI}{fg('FFDD00')}m●{CSI}0m"
yellowOff = f"{CSI}{fg('FF0000')}m●{CSI}0m"
print(yellowOn, yellowOff)
greenOn = f"{CSI}{fg('00FF88')}m●{CSI}0m"
greenOff = f"{CSI}{fg('006633')}m●{CSI}0m"
print(greenOn, greenOff)
