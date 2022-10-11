d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.position_pen(2,1)
d.curve(Direction.N, Orient.right, Length.short, Radius.medium)

d.end()
