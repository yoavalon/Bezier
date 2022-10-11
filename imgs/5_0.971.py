d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(3,2)

d.end()
