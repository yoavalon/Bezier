d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.NE, Length.short)
d.position_pen(3,0)
d.straight_line(Direction.NE, Length.short)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.W, Orient.left, Length.short, Radius.low)

d.end()
