d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.position_pen(3,1)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(3,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.E, Length.medium)

d.end()
