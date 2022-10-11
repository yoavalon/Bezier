d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.position_pen(3,1)

d.end()
