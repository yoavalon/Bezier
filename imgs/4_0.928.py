d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(0,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)

d.end()
