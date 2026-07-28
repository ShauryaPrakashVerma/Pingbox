from collections import deque
from queue import Queue


message_history = deque(maxlen=20)
message_queue = Queue()


