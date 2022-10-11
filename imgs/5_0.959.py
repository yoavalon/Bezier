d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,1)
d.position_pen(3,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.short)

d.end()
