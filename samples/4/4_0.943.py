d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.short, Radius.low)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.position_pen(1,2)
d.straight_line(Direction.W, Length.short)
d.straight_line(Direction.NW, Length.long)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.NW, Length.medium)

d.end()
