d = DslBezier()

d.position_pen(2,3)
d.position_pen(2,1)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.N, Length.medium)

d.end()
