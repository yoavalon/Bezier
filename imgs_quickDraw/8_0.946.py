d = DslBezier()

d.position_pen(0,0)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.short, Radius.medium)

d.end()
