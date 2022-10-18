d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.position_pen(3,3)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)

d.end()
