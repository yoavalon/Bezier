d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)

d.end()
