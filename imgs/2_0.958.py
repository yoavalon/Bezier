d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.long)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,1)

d.end()
