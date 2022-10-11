d = DslBezier()

d.position_pen(3,1)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(3,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)

d.end()
