d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,3)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.position_pen(1,2)
d.straight_line(Direction.N, Length.short)

d.end()
