d = DslBezier()

d.position_pen(1,0)
d.position_pen(1,2)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
