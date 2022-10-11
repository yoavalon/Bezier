d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,3)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.N, Length.medium)

d.end()
