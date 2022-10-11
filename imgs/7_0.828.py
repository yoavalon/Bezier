d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.SW, Length.short)
d.position_pen(0,0)
d.straight_line(Direction.E, Length.short)

d.end()
