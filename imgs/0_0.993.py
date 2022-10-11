d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.W, Length.medium)

d.end()
