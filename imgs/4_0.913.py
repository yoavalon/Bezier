d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,1)

d.end()
