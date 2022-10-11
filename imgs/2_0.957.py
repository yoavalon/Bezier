d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.position_pen(0,1)
d.straight_line(Direction.E, Length.short)
d.position_pen(2,2)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.NW, Length.short)

d.end()
