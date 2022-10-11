d = DslBezier()

d.position_pen(0,3)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.position_pen(0,1)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.short, Radius.medium)

d.end()
