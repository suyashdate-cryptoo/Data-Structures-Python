# ==========================================
# Queue Basics in Python
# ==========================================

# A Queue follows the FIFO principle:
# First In, First Out

# ------------------------------------------
# Create Queue
# ------------------------------------------

queue = []

# ------------------------------------------
# Enqueue Operation
# ------------------------------------------

queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after Enqueue Operations:")
print(queue)

# ------------------------------------------
# Front Element
# ------------------------------------------

if queue:
    print("\nFront Element:", queue[0])

# ------------------------------------------
# Dequeue Operation
# ------------------------------------------

removed_element = queue.pop(0)

print("\nDequeued Element:", removed_element)

# ------------------------------------------
# Final Queue
# ------------------------------------------

print("\nQueue after Dequeue:")
print(queue)



Expected Output
Queue after Enqueue Operations:
[10, 20, 30]

Front Element: 10

Dequeued Element: 10

Queue after Dequeue:
[20, 30]
