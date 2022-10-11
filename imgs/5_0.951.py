d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)

d.end()
