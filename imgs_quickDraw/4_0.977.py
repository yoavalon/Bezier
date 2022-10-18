d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)
d.position_pen(3,1)
d.position_pen(0,1)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NW, Length.medium)

d.end()
