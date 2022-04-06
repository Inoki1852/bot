import re

text = re.findall(r'by (\w+)', "Message.  by ikoni1852")
print(text)
