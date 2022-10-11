d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.position_pen(2,3)
d.position_pen(2,2)
d.straight_line(Direction.W, Length.short)

d.end()
