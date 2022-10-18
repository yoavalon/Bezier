d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.SE, Orient.left, Length.short, Radius.low)
d.curve(Direction.E, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,2)
d.position_pen(1,3)

d.end()
