d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,1)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)

d.end()
