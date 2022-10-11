d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.W, Length.short)
d.position_pen(0,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.N, Length.short)

d.end()
