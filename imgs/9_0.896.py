d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,0)
d.straight_line(Direction.W, Length.medium)
d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)

d.end()
