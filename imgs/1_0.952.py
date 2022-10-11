d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.S, Orient.left, Length.long, Radius.low)
d.position_pen(3,1)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)
d.position_pen(3,2)

d.end()
