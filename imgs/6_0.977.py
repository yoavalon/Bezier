d = DslBezier()

d.position_pen(3,1)
d.position_pen(1,1)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.short)
d.position_pen(2,1)

d.end()
