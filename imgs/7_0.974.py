d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(1,1)
d.curve(Direction.NW, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.E, Length.long)
d.straight_line(Direction.SW, Length.short)
d.position_pen(3,1)

d.end()
