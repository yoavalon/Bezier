d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.E, Length.medium)

d.end()
