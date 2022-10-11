d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)

d.end()
