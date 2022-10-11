d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.E, Length.short)

d.end()
