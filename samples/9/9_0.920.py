d = DslBezier()

d.position_pen(1,1)
d.position_pen(2,1)
d.straight_line(Direction.NE, Length.short)
d.position_pen(3,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.position_pen(3,2)
d.position_pen(0,2)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(2,2)

d.end()
