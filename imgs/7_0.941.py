d = DslBezier()

d.position_pen(1,1)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.short)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.W, Length.medium)

d.end()
