d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.position_pen(1,2)
d.straight_line(Direction.S, Length.long)
d.curve(Direction.NE, Orient.left, Length.long, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.W, Length.long)
d.straight_line(Direction.W, Length.short)

d.end()
