d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NW, Length.short)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,2)

d.end()
