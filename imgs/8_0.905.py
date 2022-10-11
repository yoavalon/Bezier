d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)
d.position_pen(3,1)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.S, Length.long)

d.end()
