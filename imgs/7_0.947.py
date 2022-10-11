d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
