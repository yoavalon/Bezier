d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.SE, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.high)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)

d.end()
