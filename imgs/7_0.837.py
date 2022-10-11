d = DslBezier()

d.position_pen(2,1)
d.position_pen(2,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.short)

d.end()
