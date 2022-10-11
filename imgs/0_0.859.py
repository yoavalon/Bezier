d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,3)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,1)
d.curve(Direction.S, Orient.right, Length.long, Radius.high)

d.end()
