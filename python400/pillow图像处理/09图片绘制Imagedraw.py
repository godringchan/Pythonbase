from PIL import Image, ImageDraw, ImageFont

new_pic = Image.new("RGB", (200, 200), "white")
drw = ImageDraw.Draw(new_pic)
drw.rectangle((50, 50, 150, 150), outline="red", fill="yellow")
font = ImageFont.truetype("SIMLI.TTF", 20)
drw.text((60, 60), font=font, text="小玉", fill="green")

new_pic.show()
