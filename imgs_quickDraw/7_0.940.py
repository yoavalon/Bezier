d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.W, Length.medium)
d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.position_pen(0,2)
d.straight_line(Direction.E, Length.short)

d.end()
