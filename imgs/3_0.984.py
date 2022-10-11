d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.SE, Length.short)
d.position_pen(1,0)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)

d.end()
