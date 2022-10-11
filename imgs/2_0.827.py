d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(3,2)
d.curve(Direction.NW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.position_pen(3,2)
d.straight_line(Direction.SE, Length.medium)

d.end()
