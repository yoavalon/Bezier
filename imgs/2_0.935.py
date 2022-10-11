d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.NE, Length.short)
d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.position_pen(0,1)

d.end()
