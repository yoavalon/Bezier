d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.S, Length.short)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)

d.end()
