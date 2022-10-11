d = DslBezier()

d.position_pen(1,1)
d.position_pen(2,3)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.position_pen(1,2)
d.straight_line(Direction.N, Length.medium)
d.position_pen(0,2)
d.straight_line(Direction.NW, Length.long)

d.end()
