d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(3,2)
d.position_pen(2,3)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)

d.end()
