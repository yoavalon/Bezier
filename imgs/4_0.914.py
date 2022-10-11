d = DslBezier()

d.position_pen(3,0)
d.position_pen(2,3)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.position_pen(2,2)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(3,2)

d.end()
