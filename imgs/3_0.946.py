d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.short)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)

d.end()
