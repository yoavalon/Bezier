d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)

d.end()
