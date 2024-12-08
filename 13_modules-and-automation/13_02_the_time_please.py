# Use a built-in Python module to tell you the current date and time.
# Research online, so you can print it in a readable manner.
from datetime import datetime
es = datetime.now()

print(es.strftime('%a %d %b %Y- %I:%M:%S.%f%p'))
#print(datetime.now())
print(es)