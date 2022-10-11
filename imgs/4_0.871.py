d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.N, Length.short)
d.position_pen(2,2)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)
d.position_pen(2,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,3)

d.end()
