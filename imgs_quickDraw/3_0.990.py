d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(0,2)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,2)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.medium)

d.end()
