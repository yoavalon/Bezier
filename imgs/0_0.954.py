d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.NE, Length.short)

d.end()
