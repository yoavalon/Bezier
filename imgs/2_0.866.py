d = DslBezier()

d.position_pen(0,2)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.high)
d.position_pen(2,3)
d.curve(Direction.S, Orient.left, Length.medium, Radius.high)
d.position_pen(1,1)

d.end()
