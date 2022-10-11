d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.NW, Length.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,3)
d.straight_line(Direction.NE, Length.medium)

d.end()
