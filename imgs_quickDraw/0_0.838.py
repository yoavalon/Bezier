d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.curve(Direction.S, Orient.right, Length.long, Radius.medium)
d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.low)

d.end()
