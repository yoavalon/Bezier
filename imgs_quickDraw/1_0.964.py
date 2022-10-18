d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.W, Length.long)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)

d.end()
