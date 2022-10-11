d = DslBezier()

d.position_pen(1,3)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,1)

d.end()
