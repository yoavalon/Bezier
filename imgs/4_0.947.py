d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.N, Length.short)
d.straight_line(Direction.W, Length.short)

d.end()
