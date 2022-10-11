d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.W, Orient.left, Length.medium, Radius.medium)
d.position_pen(3,2)
d.curve(Direction.SW, Orient.left, Length.long, Radius.medium)
d.position_pen(3,0)

d.end()
