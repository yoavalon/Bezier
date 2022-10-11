d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.SW, Length.long)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)

d.end()
