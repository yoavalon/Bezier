d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.low)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)
d.curve(Direction.N, Orient.right, Length.short, Radius.high)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)

d.end()
