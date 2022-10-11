d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.position_pen(1,1)

d.end()
