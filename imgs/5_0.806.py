d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.S, Length.short)
d.position_pen(0,3)

d.end()
