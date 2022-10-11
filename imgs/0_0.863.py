d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.position_pen(2,1)

d.end()
