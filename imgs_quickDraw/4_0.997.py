d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.NW, Orient.left, Length.short, Radius.high)
d.position_pen(1,2)

d.end()
