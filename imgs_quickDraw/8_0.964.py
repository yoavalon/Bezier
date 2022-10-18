d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.short)
d.position_pen(3,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)

d.end()
