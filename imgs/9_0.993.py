d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.W, Length.medium)

d.end()
