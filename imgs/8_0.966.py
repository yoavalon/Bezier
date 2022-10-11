d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.position_pen(2,1)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.N, Orient.left, Length.short, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.W, Length.long)

d.end()
