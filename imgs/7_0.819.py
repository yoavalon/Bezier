d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.low)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.high)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)

d.end()
