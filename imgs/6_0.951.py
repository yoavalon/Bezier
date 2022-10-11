d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.E, Orient.right, Length.short, Radius.high)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.high)
d.curve(Direction.SW, Orient.right, Length.long, Radius.high)
d.position_pen(1,2)

d.end()
