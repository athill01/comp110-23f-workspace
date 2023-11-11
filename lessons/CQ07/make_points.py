"""Checking point.py."""

from lessons.CQ07.point import Point

my_point: Point = Point(4, 7)

my_point.scale_by(2)

print(my_point.x)
print(my_point.y)

my_new_point: Point = my_point.scale(2)

print(my_new_point.x)
print(my_new_point.y)