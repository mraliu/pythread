import threading
from datetime import datetime
import time

def timer(id, num):
	for _ in range(num):
		c = datetime.now()
		current_time = c.strftime('%H:%M:%S')
		print(id, current_time)
		time.sleep(1)


if __name__ =="__main__":
	t1 = threading.Thread(target=timer, args=("a",10,))
	t2 = threading.Thread(target=timer, args=("b",5,))

	t1.start()
	t2.start()

	t1.join()
	t2.join()

	print("Done!")
