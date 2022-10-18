d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
