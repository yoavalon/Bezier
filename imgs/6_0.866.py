d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,3)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)

d.end()
