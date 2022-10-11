d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.SW, Orient.left, Length.long, Radius.high)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.short, Radius.low)
d.position_pen(2,0)

d.end()
