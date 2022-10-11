d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.position_pen(2,1)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.position_pen(1,0)

d.end()
