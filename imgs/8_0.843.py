d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.E, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,0)
d.curve(Direction.W, Orient.left, Length.long, Radius.high)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.medium)

d.end()
