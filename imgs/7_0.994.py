d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.W, Orient.left, Length.long, Radius.low)
d.straight_line(Direction.W, Length.short)
d.position_pen(3,2)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.medium, Radius.low)

d.end()
