d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)
d.curve(Direction.N, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.NW, Length.medium)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.position_pen(3,3)

d.end()
