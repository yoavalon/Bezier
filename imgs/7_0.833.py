d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.position_pen(2,2)
d.position_pen(0,1)

d.end()
