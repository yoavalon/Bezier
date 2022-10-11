d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.short, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.N, Length.long)

d.end()
