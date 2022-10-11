d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,1)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)

d.end()
