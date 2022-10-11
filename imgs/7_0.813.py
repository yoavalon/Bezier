d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.N, Length.medium)
d.position_pen(1,3)
d.curve(Direction.NW, Orient.left, Length.long, Radius.low)
d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)

d.end()
