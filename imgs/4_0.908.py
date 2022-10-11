d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.low)
d.curve(Direction.NW, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.short)

d.end()
