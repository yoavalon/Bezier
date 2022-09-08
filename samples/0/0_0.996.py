d = DslBezier()

d.position_pen(2,3)
d.position_pen(3,2)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.position_pen(2,0)
d.position_pen(2,0)

d.end()
