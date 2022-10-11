d = DslBezier()

d.position_pen(2,0)
d.position_pen(3,1)
d.straight_line(Direction.E, Length.medium)
d.position_pen(1,2)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,2)

d.end()
