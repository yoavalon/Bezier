d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.curve(Direction.NW, Orient.left, Length.short, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.S, Length.short)

d.end()
