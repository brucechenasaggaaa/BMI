weight = input('請輸入您的體重(公斤)')
height = input('請輸入您的身高(公分)')
weight = int(weight)
height = int(height)
height = height/100
bmi = weight / (height * height)
if bmi < 18.5:
	print('你的bmi值為', bmi, '屬體重過輕')
elif bmi >= 18.5 and bmi < 24:
    print('你的bmi值為', bmi, '屬正常範圍')
elif bmi >= 24 and bmi < 27:
    print('你的bmi值為', bmi, '稍重')
elif bmi >= 27 and bmi < 30:
    print('你的bmi值為', bmi, '輕度肥胖')
elif bmi >= 30 and bmi < 35:
    print('你的bmi值為', bmi, '中度肥胖')
elif bmi >= 35:
    print('你的bmi值為', bmi, '重度肥胖')