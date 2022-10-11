d = DslBezier()

d.position_pen(3,1)
d.position_pen(1,1)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,0)
d.curve(Direction.N, Orient.right, Length.medium, Radius.high)
d.position_pen(1,0)

d.end()
