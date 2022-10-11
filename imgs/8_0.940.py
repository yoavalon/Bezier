d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,0)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.S, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.S, Length.short)

d.end()
