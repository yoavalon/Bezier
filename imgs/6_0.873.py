d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(3,2)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
