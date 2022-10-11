d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.E, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,0)

d.end()
