d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.position_pen(1,2)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)

d.end()
