d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,3)
d.curve(Direction.SW, Orient.right, Length.short, Radius.low)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.high)

d.end()
