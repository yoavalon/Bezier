d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NW, Orient.right, Length.short, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.position_pen(0,0)

d.end()
