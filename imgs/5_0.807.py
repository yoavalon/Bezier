d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.straight_line(Direction.W, Length.short)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.position_pen(1,3)
d.straight_line(Direction.W, Length.medium)

d.end()
