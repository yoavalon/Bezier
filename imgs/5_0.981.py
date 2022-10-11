d = DslBezier()

d.position_pen(0,1)
d.position_pen(3,2)
d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)

d.end()
