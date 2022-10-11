d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SW, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.E, Length.medium)
d.position_pen(0,0)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.curve(Direction.SE, Orient.left, Length.long, Radius.high)

d.end()
