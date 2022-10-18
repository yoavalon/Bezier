d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.low)
d.position_pen(0,2)
d.straight_line(Direction.S, Length.long)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.NW, Length.long)

d.end()
