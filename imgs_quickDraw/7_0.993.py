d = DslBezier()

d.position_pen(1,2)
d.position_pen(3,1)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.short, Radius.low)

d.end()
