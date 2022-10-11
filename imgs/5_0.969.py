d = DslBezier()

d.position_pen(2,2)
d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)

d.end()
