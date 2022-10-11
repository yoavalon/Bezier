d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.position_pen(2,1)

d.end()
