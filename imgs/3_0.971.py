d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.S, Length.short)
d.curve(Direction.S, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SW, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.W, Length.medium)

d.end()
