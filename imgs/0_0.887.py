d = DslBezier()

d.position_pen(3,2)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(0,1)

d.end()
