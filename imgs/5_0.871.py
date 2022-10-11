d = DslBezier()

d.position_pen(1,1)
d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.position_pen(1,2)

d.end()
