d = DslBezier()

d.position_pen(2,3)
d.position_pen(0,1)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.position_pen(3,2)

d.end()
