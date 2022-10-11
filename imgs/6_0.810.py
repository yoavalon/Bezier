d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(3,1)

d.end()
