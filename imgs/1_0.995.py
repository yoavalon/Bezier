d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.N, Length.medium)

d.end()
