d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,1)
d.straight_line(Direction.S, Length.medium)

d.end()
