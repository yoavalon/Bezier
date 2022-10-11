d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,0)
d.position_pen(0,1)
d.straight_line(Direction.S, Length.medium)

d.end()
