d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.E, Length.short)
d.position_pen(3,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,2)
d.straight_line(Direction.E, Length.short)

d.end()
