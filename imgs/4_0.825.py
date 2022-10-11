d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.E, Length.short)
d.position_pen(2,1)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,0)

d.end()
