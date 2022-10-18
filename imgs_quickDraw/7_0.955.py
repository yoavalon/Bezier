d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.N, Length.short)
d.position_pen(3,3)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)

d.end()
