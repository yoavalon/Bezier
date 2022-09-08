d = DslBezier()

d.position_pen(1,2)
d.position_pen(1,1)
d.position_pen(1,2)
d.position_pen(3,0)
d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.S, Length.medium)

d.end()
