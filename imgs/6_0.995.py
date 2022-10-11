d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.high)
d.curve(Direction.NW, Orient.left, Length.short, Radius.high)
d.position_pen(0,3)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.E, Length.medium)

d.end()
