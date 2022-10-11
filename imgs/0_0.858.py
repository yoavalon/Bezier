d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.low)
d.curve(Direction.N, Orient.left, Length.long, Radius.medium)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.low)

d.end()
