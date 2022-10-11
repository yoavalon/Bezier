d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.left, Length.short, Radius.high)
d.curve(Direction.N, Orient.left, Length.long, Radius.high)
d.position_pen(2,0)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)

d.end()
