d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.right, Length.short, Radius.medium)
d.position_pen(1,1)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.position_pen(2,3)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.position_pen(0,1)

d.end()
