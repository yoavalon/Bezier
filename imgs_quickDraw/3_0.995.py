d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,3)

d.end()
