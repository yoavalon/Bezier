d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)
d.position_pen(1,2)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.medium)

d.end()
