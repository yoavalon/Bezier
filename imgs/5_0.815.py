d = DslBezier()

d.position_pen(0,2)
d.position_pen(3,0)
d.curve(Direction.E, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)
d.position_pen(2,1)

d.end()
