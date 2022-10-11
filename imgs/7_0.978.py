d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.N, Length.long)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.NE, Length.medium)

d.end()
