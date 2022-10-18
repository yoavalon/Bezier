d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.short)

d.end()
