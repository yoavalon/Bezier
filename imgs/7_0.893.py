d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.N, Length.short)

d.end()
