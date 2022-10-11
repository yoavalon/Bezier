d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.high)
d.curve(Direction.NW, Orient.left, Length.long, Radius.high)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.N, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)

d.end()
