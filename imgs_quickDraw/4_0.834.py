d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.position_pen(0,2)

d.end()
