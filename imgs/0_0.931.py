d = DslBezier()

d.position_pen(3,1)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)
d.position_pen(1,3)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,2)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(3,0)

d.end()
