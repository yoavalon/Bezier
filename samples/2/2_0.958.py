d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.NW, Length.long)
d.position_pen(2,1)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.high)
d.position_pen(1,3)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.medium)
d.position_pen(2,1)

d.end()
