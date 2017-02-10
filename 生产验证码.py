import string,random
import Image,ImageDraw,ImageFont,ImageFilter
fontPath = "c://Windows/Fonts/"
def getNumber():
	return [random.choice(string.letters) for _ in range(4)]
def getColor():
	return (random.randint(30,100),random.randint(30,100),random.randint(30,100))
x = raw_input('please input a number for yanzhengma?\n')
def getPic():
	width = 240
	height = 60
	image = Image.new('RGB',(width,height),(180,180,180))
	font = ImageFont.truetype(fontPath+'Verdana.ttf',40)
	draw = ImageDraw.Draw(image)
	code = getNumber()
	for t in range(4):
		draw.text((60*t+10,0),code[t],font=font,fill=getColor())
	for _ in range(4):
		draw.point((random.randint(0,width),random.randint(0,height)),fill=getColor())
	image = image.filter(ImageFilter.BLUR)
	image.save('h://database/yanzhengma/'+"".join(code)+'.jpg','jpeg')
if __name__=='__main__':
	for i in range(int(x)):
		getPic()
    
    批量生产验证码：输入会有提示需要产生的验证码图片数量。（pic库，随机数库还有字符串库）
