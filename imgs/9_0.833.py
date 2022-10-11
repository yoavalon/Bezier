d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)

d.end()
