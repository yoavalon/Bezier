d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)
d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)

d.end()
