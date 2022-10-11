d = DslBezier()

d.position_pen(0,1)
d.position_pen(1,3)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)

d.end()
