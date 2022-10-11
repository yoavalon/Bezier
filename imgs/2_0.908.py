d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.position_pen(1,1)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.high)
d.curve(Direction.SE, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)

d.end()
