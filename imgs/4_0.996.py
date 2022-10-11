d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.SE, Length.short)
d.position_pen(2,2)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.position_pen(3,2)

d.end()
