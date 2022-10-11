d = DslBezier()

d.position_pen(2,3)
d.position_pen(2,0)
d.curve(Direction.NE, Orient.left, Length.medium, Radius.high)
d.position_pen(1,0)
d.curve(Direction.E, Orient.left, Length.short, Radius.low)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.position_pen(1,0)

d.end()
