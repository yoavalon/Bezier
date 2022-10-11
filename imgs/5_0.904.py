d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.S, Length.short)

d.end()
