d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.E, Orient.right, Length.short, Radius.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)
d.straight_line(Direction.W, Length.long)

d.end()
