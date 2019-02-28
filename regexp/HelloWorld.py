import re

txt = "<a>你好<p>你也好~</p></a><img src='asdfasdfasdfdf'>"
x = re.findall('(<a.*>*.*</a>)|(<img.*/>)|(<img.*>)', txt)
label_a = set()
label_img = set()
for a, image, c in x:
    label_a.add(a)
    label_img.add(image)
    label_img.add(c)

print(label_a)
print(label_img)
