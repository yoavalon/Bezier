d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.short)
d.position_pen(1,3)
d.curve(Direction.W, Orient.right, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.short)

d.end()
