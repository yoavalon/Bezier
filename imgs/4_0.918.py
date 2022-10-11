d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.N, Length.long)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,1)

d.end()
