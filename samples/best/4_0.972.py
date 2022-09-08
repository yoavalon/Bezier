d = DslBezier()

d.position_pen(3,0)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,3)
d.position_pen(1,2)
d.position_pen(2,0)
d.position_pen(1,3)
d.curve(Direction.S, Orient.left, Length.short, Radius.low)

d.end()
