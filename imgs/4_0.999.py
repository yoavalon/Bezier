d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.SW, Length.short)

d.end()
