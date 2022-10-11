d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.position_pen(0,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,2)

d.end()
