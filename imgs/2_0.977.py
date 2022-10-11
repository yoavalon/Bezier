d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.position_pen(1,2)

d.end()
