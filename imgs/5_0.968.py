d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.medium)

d.end()
