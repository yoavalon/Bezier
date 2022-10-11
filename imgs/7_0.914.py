d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.position_pen(1,3)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.S, Length.long)

d.end()
