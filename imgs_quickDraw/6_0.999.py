d = DslBezier()

d.position_pen(3,3)
d.straight_line(Direction.N, Length.short)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.straight_line(Direction.N, Length.long)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.long)

d.end()
