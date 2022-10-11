d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.E, Length.long)

d.end()
