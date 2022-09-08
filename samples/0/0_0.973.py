d = DslBezier()

d.position_pen(2,3)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,3)
d.position_pen(3,3)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,2)

d.end()
