d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.SE, Length.long)
d.position_pen(0,1)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.N, Orient.left, Length.medium, Radius.medium)

d.end()
