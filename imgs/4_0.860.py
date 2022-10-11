d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NW, Length.long)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.short)
d.position_pen(2,3)
d.straight_line(Direction.E, Length.short)

d.end()
