d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)
d.position_pen(2,1)
d.straight_line(Direction.W, Length.long)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.SW, Length.medium)
d.curve(Direction.N, Orient.left, Length.long, Radius.low)

d.end()
