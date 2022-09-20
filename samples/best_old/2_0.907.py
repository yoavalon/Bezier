d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.position_pen(0,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
