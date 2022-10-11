d = DslBezier()

d.position_pen(2,3)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,2)
d.position_pen(2,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)

d.end()
