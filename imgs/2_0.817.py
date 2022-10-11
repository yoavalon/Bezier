d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.position_pen(2,1)
d.straight_line(Direction.S, Length.medium)
d.position_pen(2,1)

d.end()
