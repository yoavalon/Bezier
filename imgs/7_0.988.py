d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.N, Length.medium)
d.position_pen(2,0)

d.end()
