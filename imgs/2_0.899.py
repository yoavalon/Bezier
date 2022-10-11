d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.W, Orient.left, Length.long, Radius.high)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,1)

d.end()
