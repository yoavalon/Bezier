d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.high)

d.end()
