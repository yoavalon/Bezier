d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.medium)

d.end()
