d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.position_pen(2,1)
d.straight_line(Direction.N, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)

d.end()
