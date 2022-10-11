d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.position_pen(0,3)

d.end()
