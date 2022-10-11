d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.position_pen(3,2)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.position_pen(1,1)

d.end()
