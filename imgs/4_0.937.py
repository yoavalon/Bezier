d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(3,1)
d.straight_line(Direction.E, Length.medium)

d.end()
