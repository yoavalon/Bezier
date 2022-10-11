d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.position_pen(1,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
