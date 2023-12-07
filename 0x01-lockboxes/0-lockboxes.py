#!/usr/bin/python3
"""
You have n number of locked boxes in front of you. Each box is numbered
sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
"""

def canUnlockAll(boxes):
	""" method that determines if all the boxes can be opened"""
	unlocked_boxes = [False] * len(boxes)
	unlocked_boxes[0] = True
	stack = set(boxes[0])
	while stack:
		key = stack.pop()

		if key < len(boxes) and not unlocked_boxes[key]:
			unlocked_boxes[key] = True
			stack.update(boxes[key])

	return all(unlocked_boxes)



