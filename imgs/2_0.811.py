d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(2,0)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.N, Orient.left, Length.short, Radius.high)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.W, Length.medium)

d.end()
