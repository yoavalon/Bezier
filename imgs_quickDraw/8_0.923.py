d = DslBezier()

d.position_pen(2,2)
d.position_pen(0,2)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)

d.end()
