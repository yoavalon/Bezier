d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(3,2)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)

d.end()
