d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.E, Length.medium)
d.position_pen(3,1)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(3,1)

d.end()
