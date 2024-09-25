import time

total_seconds = input("타이머 시간을 입력하세요: ")
while not(total_seconds.isdigit()):
  total_seconds = input("타이머 시간을 숫자로만 입력하세요: ")
total_seconds = int(total_seconds)
seconds = total_seconds % 60
minutes = total_seconds // 60

# range(minutes + 1)[::-1] == range(minutes, -1, -1)
for m in range(minutes + 1)[::-1]:
  if m != minutes:
    seconds = 59
  for s in reversed(range(seconds + 1)):
    print(f"00:{m:02d}:{s:02d}")
    time.sleep(1)