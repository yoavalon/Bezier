d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.position_pen(3,1)
d.position_pen(2,2)

d.end()
