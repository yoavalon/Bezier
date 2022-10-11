d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.short)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)
d.position_pen(1,0)
d.straight_line(Direction.NE, Length.long)

d.end()
