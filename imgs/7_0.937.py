d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.medium)
d.position_pen(3,0)
d.position_pen(0,3)

d.end()
