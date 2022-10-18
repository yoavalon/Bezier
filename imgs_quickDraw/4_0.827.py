d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,2)

d.end()
