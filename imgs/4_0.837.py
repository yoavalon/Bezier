d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.long)

d.end()
