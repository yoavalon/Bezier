d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.NE, Orient.left, Length.short, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(2,1)
d.position_pen(0,2)

d.end()
