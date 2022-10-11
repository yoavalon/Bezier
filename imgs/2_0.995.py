d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.W, Orient.left, Length.long, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.right, Length.medium, Radius.high)

d.end()
