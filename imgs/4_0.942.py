d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,3)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.position_pen(0,3)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)

d.end()
