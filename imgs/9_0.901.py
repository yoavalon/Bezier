d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.position_pen(2,1)

d.end()
