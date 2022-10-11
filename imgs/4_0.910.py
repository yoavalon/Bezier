d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)
d.curve(Direction.E, Orient.left, Length.short, Radius.high)
d.straight_line(Direction.SW, Length.medium)

d.end()
