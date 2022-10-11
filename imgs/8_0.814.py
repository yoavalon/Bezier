d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,0)
d.curve(Direction.W, Orient.left, Length.short, Radius.high)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.W, Length.long)

d.end()
