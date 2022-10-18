d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.low)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.N, Length.medium)

d.end()
