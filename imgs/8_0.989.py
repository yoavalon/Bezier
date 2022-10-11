d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.short)

d.end()
