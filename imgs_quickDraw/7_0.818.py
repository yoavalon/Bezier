d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.E, Length.short)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.high)

d.end()
