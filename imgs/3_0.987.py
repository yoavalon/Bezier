d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.N, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.NW, Length.short)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.position_pen(2,0)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.W, Orient.left, Length.long, Radius.medium)

d.end()
