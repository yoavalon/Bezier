d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)

d.end()
