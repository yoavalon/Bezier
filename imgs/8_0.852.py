d = DslBezier()

d.position_pen(3,1)
d.position_pen(1,2)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)

d.end()
