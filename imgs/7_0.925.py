d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.position_pen(2,1)

d.end()
