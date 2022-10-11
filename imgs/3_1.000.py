d = DslBezier()

d.position_pen(0,1)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
