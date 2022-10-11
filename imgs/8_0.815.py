d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)
d.position_pen(1,0)
d.curve(Direction.S, Orient.left, Length.short, Radius.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.low)

d.end()
