d = DslBezier()

d.position_pen(1,0)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)
d.curve(Direction.W, Orient.left, Length.medium, Radius.low)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)

d.end()
