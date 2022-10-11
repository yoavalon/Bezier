d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.low)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.SW, Orient.right, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)

d.end()
