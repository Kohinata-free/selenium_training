from PIL import Image
import pyocr
import pyocr.builders

tools = pyocr.get_available_tools()
tool = tools[0]
builder = pyocr.builders.TextBuilder()

image = Image.open("image.png")
text = tool.image_to_string(image, lang="jpn", builder=builder)
# text = tool.image_to_string(image, lang="eng", builder=builder)
lst = text.split("\n")
print(lst)