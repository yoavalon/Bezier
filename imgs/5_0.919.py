d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.position_pen(2,0)

d.end()
