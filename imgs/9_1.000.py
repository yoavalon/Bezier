d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.NE, Length.medium)

d.end()
