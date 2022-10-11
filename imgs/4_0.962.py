d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.E, Length.medium)
d.position_pen(0,3)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(1,2)
d.position_pen(2,0)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)

d.end()
