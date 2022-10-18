d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(1,0)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,2)
d.position_pen(3,0)

d.end()
