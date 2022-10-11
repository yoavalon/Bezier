d = DslBezier()

d.position_pen(0,2)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.N, Orient.right, Length.short, Radius.low)
d.curve(Direction.N, Orient.left, Length.long, Radius.medium)

d.end()
