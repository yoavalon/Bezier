d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.NE, Length.short)
d.position_pen(1,3)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.N, Length.long)

d.end()
