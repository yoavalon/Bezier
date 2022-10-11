d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
