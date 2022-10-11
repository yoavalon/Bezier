d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.long)
d.position_pen(0,3)

d.end()
