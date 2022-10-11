d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)

d.end()
