d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.SW, Length.short)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.S, Length.short)
d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)

d.end()
