d = DslBezier()

d.position_pen(1,1)
d.position_pen(2,0)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(1,0)
d.straight_line(Direction.SE, Length.medium)

d.end()
