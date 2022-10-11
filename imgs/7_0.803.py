d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.long)
d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.long, Radius.low)
d.position_pen(0,2)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.SE, Length.medium)

d.end()
