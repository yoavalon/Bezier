d = DslBezier()

d.position_pen(1,2)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.E, Length.medium)

d.end()
