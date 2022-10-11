d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.position_pen(2,3)
d.straight_line(Direction.N, Length.medium)
d.position_pen(3,0)
d.position_pen(3,2)

d.end()
