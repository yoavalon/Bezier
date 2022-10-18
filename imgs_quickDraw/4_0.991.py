d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.position_pen(1,3)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.E, Length.short)

d.end()
