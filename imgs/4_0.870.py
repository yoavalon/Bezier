d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)

d.end()
