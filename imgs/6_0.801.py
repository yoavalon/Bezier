d = DslBezier()

d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.position_pen(3,2)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.SW, Orient.right, Length.long, Radius.medium)
d.position_pen(2,0)

d.end()
