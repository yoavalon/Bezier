d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.short, Radius.low)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.curve(Direction.E, Orient.right, Length.long, Radius.low)

d.end()
