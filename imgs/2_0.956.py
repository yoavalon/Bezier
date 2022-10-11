d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,2)
d.curve(Direction.W, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.NE, Length.short)

d.end()
