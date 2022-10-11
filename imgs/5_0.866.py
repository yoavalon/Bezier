d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,3)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)

d.end()
