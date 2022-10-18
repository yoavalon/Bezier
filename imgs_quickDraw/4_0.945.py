d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(0,3)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
