d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.E, Length.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.N, Orient.left, Length.medium, Radius.low)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.E, Orient.left, Length.medium, Radius.high)
d.curve(Direction.N, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.E, Length.short)
d.straight_line(Direction.E, Length.short)

d.end()
