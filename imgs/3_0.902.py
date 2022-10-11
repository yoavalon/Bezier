d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)

d.end()
