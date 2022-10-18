d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)
d.position_pen(2,1)
d.position_pen(1,1)
d.straight_line(Direction.E, Length.short)
d.position_pen(3,2)

d.end()
