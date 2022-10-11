d = DslBezier()

d.position_pen(2,1)
d.straight_line(Direction.S, Length.long)
d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)

d.end()
