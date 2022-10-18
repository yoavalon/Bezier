d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NW, Orient.right, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)

d.end()
