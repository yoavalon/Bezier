d = DslBezier()

d.position_pen(1,2)
d.position_pen(0,2)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)

d.end()
