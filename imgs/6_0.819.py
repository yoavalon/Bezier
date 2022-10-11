d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,2)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)
d.position_pen(3,3)

d.end()
