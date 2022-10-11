d = DslBezier()

d.position_pen(3,0)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.S, Length.short)

d.end()
