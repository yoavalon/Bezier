d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.long)

d.end()
