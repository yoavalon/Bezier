d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.long)
d.position_pen(1,3)
d.straight_line(Direction.NE, Length.medium)

d.end()
