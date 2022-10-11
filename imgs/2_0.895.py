d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.NE, Length.short)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.NW, Length.short)

d.end()
