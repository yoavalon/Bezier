d = DslBezier()

d.position_pen(3,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,2)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.position_pen(1,2)

d.end()
