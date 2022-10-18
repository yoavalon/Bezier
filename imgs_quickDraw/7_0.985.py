d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.W, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)

d.end()
