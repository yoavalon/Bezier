d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)

d.end()
