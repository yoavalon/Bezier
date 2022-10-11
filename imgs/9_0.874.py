d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(0,1)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)

d.end()
