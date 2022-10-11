d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.NE, Length.medium)

d.end()
