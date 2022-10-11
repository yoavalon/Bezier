d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,0)
d.straight_line(Direction.E, Length.medium)

d.end()
