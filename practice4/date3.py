from datetime import datetime
now = datetime.now()
no_microseconds = now.replace(microsecond=0)

print(now)
print(no_microseconds)