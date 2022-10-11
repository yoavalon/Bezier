d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.position_pen(2,2)
d.position_pen(2,2)
d.straight_line(Direction.SW, Length.medium)

d.end()
