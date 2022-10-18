d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.high)
d.position_pen(0,3)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.high)

d.end()
