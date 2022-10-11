d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NW, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.E, Length.long)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)

d.end()
